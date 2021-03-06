// Global variables for check in modal
const openCheckIn = document.getElementById('open-checkin-modal')
const checkInModal = document.getElementById('checkin-modal')
const checkInCategory = document.getElementById('checkin-cat-select')
const xButton = document.getElementById('x-checkin-btn')
const closeCheckInBtn = document.getElementById('close-checkin')
const saveCheckInBtn = document.getElementById('save-checkin')
const checkInModalBackdrop = document.getElementById('checkin-modal-backdrop')

// Event handler to show backdrop
const toggleBackdropHandler = () => {
  checkInModalBackdrop.classList.toggle('visible')
}

// Event handler to open checkin modal
const openCheckInHandler = () => {
  checkInModal.style.display = 'block'
  toggleBackdropHandler()
}

// Event handler to close checkin modal
const saveCheckIn = () => {
  checkInModal.style.display = 'none'
  toggleBackdropHandler()
}

const closeCheckInModal = () => {
  checkInModal.style.display = 'none'
  toggleBackdropHandler()
}

// Event handler functions for check in modal inner events
const checkInHandler = () => {
  const inputLabel = document.getElementById('input-label')
  const hiddenForm = document.getElementById('checkin-form-part-two')
  if (checkInCategory.value == "Water Intake") {
    inputLabel.innerHTML = "How many oz did you drink today?"
  } else if (checkInCategory.value == "Steps") {
    inputLabel.innerHTML = "How many steps did you take today?"
  } else if (checkInCategory.value == "Heart Rate") {
    inputLabel.innerHTML = "What is your current resting heart rate?"
  } else if (checkInCategory.value == "Calories") {
    inputLabel.innerHTML = "How many calories have you had today?"
  } else if (checkInCategory.value == "Weight") {
    inputLabel.innerHTML = "What is your goal weight in pounds?"
  }
  hiddenForm.classList.remove('invisible')
}

// Event listener for check in modal
openCheckIn.addEventListener('click', openCheckInHandler)
closeCheckInBtn.addEventListener('click', closeCheckInModal)
xButton.addEventListener('click', closeCheckInModal)
saveCheckInBtn.addEventListener('click', saveCheckIn)
checkInCategory.addEventListener('change', checkInHandler)
