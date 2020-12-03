// Global constants for opening and closing add goal modal event listeners
const backdrop = document.getElementById('modal-backdrop')
const addGoalBtn = document.getElementById('start-modal-btn')
const addGoalModal = document.getElementById('add-goal-modal')
const xModalButton = document.getElementById('x-goal-button')
const saveGoalBtn = document.getElementById('save-add-goal')
const closeModalBtn = document.getElementById('stop-add-goal')

// Global constants for showing and hiding add goal form portions
const category = document.getElementById('category-select')

// Global constants for showing edit goal modal
const editGoalBtns = document.querySelectorAll('.open-edit-goal')
const editGoalModal = document.getElementById('edit-goal-modal')
const saveEditGoalBtn = document.getElementById('save-edit-goal')
const xEditGoalBtn = document.getElementById('x-edit-button')
const closeEditGoalBtn = document.getElementById('stop-edit-goal')

// Handlers for open and close add goal modal event listeners
const backdropHandler = () => {
  backdrop.classList.toggle('visible')
}

const addGoalModalHandler = () => {
  backdropHandler()
  addGoalModal.style.display = 'block'
}

const cancelAddHandler = () => {
  addGoalModal.style.display = 'none'
  backdropHandler()
}

const saveAddGoalHandler = () => {
  addGoalModal.style.display = 'none'
  backdropHandler()
}

// TODO: fix the hell that is my HTML rn and make it work

// Helper function to post goal data to back end
const postGoalData = () => {
  const goalId = document.getElementById('goal-id').value
  console.log("in postgoaldata funct")
  axios.post('/goal_data', {
    "goalId": goalId
  })
  .then(response => {
    console.log(response)
  })
  .catch(error => {
    console.log(error)
  })

}

// Helper function to dynamically get goal data
const getGoalData = (event) => {
  event.preventDefault()
  console.log("making request")
  axios.get('/goal_data')
  .then(response => {
    console.log(response)
  })
  .catch(error => {
    console.log(error)
  })
}

// Handlers for open and close edit goal modal event listeners
const editGoalModalHandler = () => {
  backdropHandler()
  editGoalModal.style.display = 'block'
  getGoalData()
}



const cancelEditHandler = () => {
  editGoalModal.style.display = 'none'
  backdropHandler()
}

const saveEditGoalHandler = () => {
  editGoalModal.style.display = 'none'
  backdropHandler()
}

// Handlers for showing and hiding portions of add goal form
const finishAddGoalHandler = () => {
  const goalLabel = document.getElementById('goal-label')
  const baselineLabel = document.getElementById('baseline-label')
  const hiddenForm = document.getElementById('goal-form-part-two')
  if (category.value == "Water Intake") {
    goalLabel.innerHTML = "How many oz per day?"
    baselineLabel.innerHTML = "How many oz per day do you drink right now?"
  } else if (category.value == "Steps") {
    goalLabel.innerHTML = "How many steps per day?"
    baselineLabel.innerHTML = "How many steps per day do you take right now?"
  } else if (category.value == "Heart Rate") {
    goalLabel.innerHTML = "What would you like your heart rate to be at rest? (Beats per minute)"
    baselineLabel.innerHTML = "About what is your current resting heart rate?"
  } else if (category.value == "Calories") {
    goalLabel.innerHTML = "How many calories per day?"
    baselineLabel.innerHTML = "About how many calories a day do you eat currently?"
  } else if (category.value == "Weight") {
    goalLabel.innerHTML = "What is your goal weight in pounds?"
    baselineLabel.innerHTML = "What is your current weight in pounds?"
  }
  hiddenForm.classList.remove('invisible')
}

category.addEventListener('change', finishAddGoalHandler)

// Event listeners for opening and closing add goal modal
addGoalBtn.addEventListener('click', addGoalModalHandler)
saveGoalBtn.addEventListener('click', saveAddGoalHandler)
xModalButton.addEventListener('click', cancelAddHandler)
closeModalBtn.addEventListener('click', cancelAddHandler)
backdrop.addEventListener('click', cancelAddHandler)

// Event listeners for opening and closeing edit goal modal
for (editGoalBtn of editGoalBtns) {
  editGoalBtn.addEventListener('click', editGoalModalHandler)
}
saveEditGoalBtn.addEventListener('click', saveEditGoalHandler)
closeEditGoalBtn.addEventListener('click', cancelEditHandler)
xEditGoalBtn.addEventListener('click', cancelEditHandler)
