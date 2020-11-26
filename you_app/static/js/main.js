// Global variables for at a glance modal
const openAtAGlanceBtn = document.getElementById('open-glance')
const atAGlance = document.getElementById('at-a-glance')

// Global variables for check in modal
const openCheckIn = document.getElementById('open-checkin-modal')
const checkInModal = document.getElementById('checkin-modal')
const category = document.getElementById('checkin-cat-select')
const xButton = document.getElementById('x-checkin-btn')
const closeCheckInBtn = document.getElementById('close-checkin')
const saveCheckInBtn = document.getElementById('save-checkin')

// Event handler to open checkin modal
const openCheckInHandler = () => {
  checkInModal.style.display = 'block'
}

// Event handler to close checkin modal
const saveCheckIn = () => {
  checkInModal.style.display = 'none'
}

const closeCheckInModal = () => {
  checkInModal.style.display = 'none'
}

// Event handler functions for check in modal inner events
const checkInHandler = () => {
  console.log('clicked')
  const inputLabel = document.getElementById('input-label')
  const hiddenForm = document.getElementById('checkin-form-part-two')
  if (category.value == "Water Intake") {
    inputLabel.innerHTML = "How many oz did you drink today?"
  } else if (category.value == "Steps") {
    inputLabel.innerHTML = "How many steps did you take today?"
  } else if (category.value == "Heart Rate") {
    inputLabel.innerHTML = "What is your current resting heart rate?"
  } else if (category.value == "Calories") {
    inputLabel.innerHTML = "How many calories have you had today?"
  } else if (category.value == "Weight") {
    inputLabel.innerHTML = "What is your goal weight in pounds?"
  }
  hiddenForm.classList.remove('invisible')
}

// At a glance opening handler func
const openGlanceHandler = () => {
  atAGlance.classList.toggle('invisible')
}

// At a glance event listener
openAtAGlanceBtn.addEventListener('click', openGlanceHandler)

// Event listener for check in modal
openCheckIn.addEventListener('click', openCheckInHandler)
closeCheckInBtn.addEventListener('click', closeCheckInModal)
xButton.addEventListener('click', closeCheckInModal)
saveCheckInBtn.addEventListener('click', saveCheckIn)
category.addEventListener('change', checkInHandler)
