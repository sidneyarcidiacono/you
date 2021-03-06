"""Build out database model classes."""
from you_app import db, login_manager
from flask_login import UserMixin
from passlib.hash import sha256_crypt
from datetime import date, datetime
import math


@login_manager.user_loader
def user_loader(user_id):
    """
    Query user from database.

    This is the user_loader func
    for flask_login.
    """
    return User.query.filter_by(id=user_id).first()


class Challenges(db.Model):
    """Create class Challenges to represent db object."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    dates = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(30), nullable=True)
    users = db.relationship("User", secondary="joined_challenges")


joined_challenges = db.Table(
    "joined_challenges",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("challenges_id", db.Integer, db.ForeignKey("challenges.id")),
)


class User(db.Model, UserMixin):
    """Create user class for login & user mgmt."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    posts = db.relationship(
        "Post", cascade="all, delete", backref="user", lazy=True
    )
    avatar = avatar = db.Column(
        db.String(30),
        nullable=False,
        default="default_profile_pic.jpg",
    )
    challenges = db.relationship("Challenges", secondary="joined_challenges")

    def set_is_admin(self):
        """Set is_admin to True under a specific condition."""
        if self.email == "sid@sid.com":
            self.is_admin = True

    def set_password(self, password):
        """Set a hashed password for insertion into db."""
        self.password = sha256_crypt.hash(password)

    def verify_password(self, password):
        """Verify hashed password for log in."""
        return sha256_crypt.verify(password, self.password)


class Post(db.Model):
    """Create class Post for user posts."""

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(30), nullable=True, default=None)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    likes = db.Column(db.Integer, default=0)


class Checkin(db.Model):
    """Model to hold check in data."""

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), nullable=False)
    amt_completed = db.Column(db.Integer, nullable=False)
    date_entered = db.Column(db.DateTime, default=date.today())
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.id"))


class Goal(db.Model):
    """Model for user goals."""

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(40), nullable=False)
    goal = db.Column(db.Integer, nullable=False, default=0)
    start_date = db.Column(db.DateTime, default=datetime.now)
    end_date = db.Column(db.DateTime, default=datetime.now)
    user_baseline = db.Column(db.Integer, default=0, nullable=False)
    daily_goal_percent = db.Column(db.Integer, default=0)
    percent_complete = db.Column(db.Integer, default=0)
    percentile_friends = db.Column(db.Integer, default=0)
    daily_expected_improvement = db.Column(db.Integer, default=0)
    set_daily_expected = db.Column(db.DateTime, default=date.today())
    daily_expected_intake = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def daily_expected(self):
        """Calculate daily expected intake/activity for user's goals."""
        # Define helper variables for calculations
        days_to_accomplish = (self.end_date - self.start_date).days
        improvement_needed = self.goal - self.user_baseline
        # If the goal is to decrease something (calorie intake, heart rate)
        # Then we need the subtraction to go the opposite way. Check for that
        # and reset our variable accordingly
        if improvement_needed < 0:
            print(f"Negative improvement needed: {improvement_needed}")
            improvement_needed = self.user_baseline - self.goal
        self.daily_expected_improvement = math.ceil(
            improvement_needed / days_to_accomplish
        )
        # This is going to return an integer. This is going to be the
        # hard number of steps towards our goal needed per day.
        # We can evaluate this based on the category that we know.
        return self.daily_expected_improvement

    def set_daily_expected_intake(self):
        """Set each day's intake/activity goal."""
        if not self.daily_expected_intake:
            self.daily_expected_intake = (
                self.user_baseline + self.daily_expected_improvement
            )
        elif (
            datetime.strptime(str(date.today()), "%Y-%m-%d")
            - self.set_daily_expected
        ).days > 1 and self.daily_expected_intake:
            self.daily_expected_intake += self.daily_expected_improvement
        return self.daily_expected_intake

    def set_daily_percent_completed(self, check_in_amt):
        """Calculate percent complete towards daily goal."""
        if not self.daily_goal_percent:
            self.daily_goal_percent = math.floor(
                (int(check_in_amt) / self.daily_expected_intake * 100)
            )
        else:
            self.daily_goal_percent += math.floor(
                (int(check_in_amt) / self.daily_expected_intake * 100)
            )
        return self.daily_goal_percent

    # TODO: Improve this function to more accurately calculate percentage

    def set_percent_completed(self):
        """Define percent progress."""
        # Define variable days to calculate days since goal was started
        days = (
            datetime.strptime(str(date.today()), "%Y-%m-%d") - self.start_date
        ).days
        # If we just started, days is just going to be 1
        if days < 1:
            days = 1

        # Query check ins so we know where the user is at in terms of progress
        all_check_ins = Checkin.query.filter_by(goal_id=self.id).all()
        # Set helper variables
        counter = 0
        result = 0
        # Check if there are check ins to look at
        if all_check_ins:
            for check_in in all_check_ins:
                # for each check in, sum the amount
                print(
                    f"Check in {check_in.id} amount {check_in.amt_completed}"
                )
                result += check_in.amt_completed
                # Increment the counter for each check in
                counter += 1
            # If our result is high for categories like calories or steps,
            # we need to normalize the data so that the percentages are stable
            # So, we'll divide these by 100
            if result > 1000:
                daily_average = math.floor((result / counter) / 100)
            else:
                # If the result is pretty normal (for all other categories)
                # we just want the average
                daily_average = math.floor(result / counter)
            # Set self.percent_complete
            self.percent_complete = math.floor((daily_average / days))
            return self.percent_complete
        # If there are no check ins, our default percent complete is 0, so
        # we just return that
        else:
            return self.percent_complete
