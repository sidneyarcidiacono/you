const openAtAGlanceBtn = document.getElementById('open-glance')
const atAGlance = document.getElementById('at-a-glance')
const openAddPostBtn = document.getElementById('open-add-post')
const backdrop = document.getElementById('post-add-backdrop')
const addPostModal = document.getElementById('add-post-modal')
const saveAddPost = document.getElementById('save-add-post')
const cancelAddPost = document.getElementById('stop-add-post')
const closeModal = document.getElementById('x-post-button')

const backdropHandler = () => {
  backdrop.classList.toggle('visible')
}

const openGlanceHandler = () => {
  atAGlance.classList.toggle('invisible')
}

const newPostHandler = () => {
  backdropHandler()
  addPostModal.classList.toggle('invisible')
}


openAtAGlanceBtn.addEventListener('click', openGlanceHandler)
openAddPostBtn.addEventListener('click', newPostHandler)
closeModal.addEventListener('click', newPostHandler)
cancelAddPost.addEventListener('click', newPostHandler)
saveAddPost.addEventListener('click', newPostHandler)
