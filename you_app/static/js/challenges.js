const startModalBtn = document.getElementById('start-modal-btn')
const addChallengeModal = document.getElementById('add-challenge-modal')
const saveChallengeBtn = document.getElementById('save-add-challenge')
const stopAddChallengeBtn = document.getElementById('stop-add-challenge')
const closeButton = document.getElementById('x-button')
const backdrop = document.getElementById('modal-backdrop')


const backdropHandler = () => {
  backdrop.classList.toggle('visible')
}

const challengeModalHandler = () => {
  backdropHandler()
  addChallengeModal.style.display = 'block'
}

const cancelAddHandler = () => {
  addChallengeModal.style.display = 'none'
  backdropHandler()
}

const saveChallengeHandler = () => {
  console.log('clicked')
  addChallengeModal.style.display = 'none'
  backdropHandler()
}

startModalBtn.addEventListener('click', challengeModalHandler)
saveChallengeBtn.addEventListener('click', saveChallengeHandler)
stopAddChallengeBtn.addEventListener('click', cancelAddHandler)
closeButton.addEventListener('click', cancelAddHandler)
backdrop.addEventListener('click', backdropHandler)
