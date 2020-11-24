const backdrop = document.getElementById('modal-backdrop')
const addGoalBtn = document.getElementById('start-modal-btn')
const addGoalModal = document.getElementById('add-goal-modal')
const xModalButton = document.getElementById('x-goal-button')
const saveGoalBtn = document.getElementById('save-add-goal')
const closeModalBtn = document.getElementById('stop-add-goal')

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

addGoalBtn.addEventListener('click', addGoalModalHandler)
saveGoalBtn.addEventListener('click', saveAddGoalHandler)
xModalButton.addEventListener('click', cancelAddHandler)
closeModalBtn.addEventListener('click', cancelAddHandler)
backdrop.addEventListener('click', cancelAddHandler)
