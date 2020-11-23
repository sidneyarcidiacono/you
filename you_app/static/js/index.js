const openAddPostBtn = document.getElementById('open-add-post')
const backdrop = document.getElementById('post-add-backdrop')
const addPostModal = document.getElementById('add-post-modal')
const saveAddPost = document.getElementById('save-add-post')
const cancelAddPost = document.getElementById('stop-add-post')
const closeModal = document.getElementById('x-post-button')

const backdropHandler = () => {
  backdrop.classList.toggle('visible')
}

const addPostModalHandler = () => {
  backdropHandler()
  addPostModal.style.display = 'block'
}

const cancelAddPostHandler = () => {
  addPostModal.style.display = 'none'
  backdropHandler()
}

const saveAddPostHandler = () => {
  addPostModal.style.display = 'none'
  backdropHandler()
}

openAddPostBtn.addEventListener('click', addPostModalHandler)
closeModal.addEventListener('click', cancelAddPostHandler)
cancelAddPost.addEventListener('click', cancelAddPostHandler)
saveAddPost.addEventListener('click', saveAddPostHandler)
