// Global variables for at a glance modal
const openAtAGlanceBtn = document.getElementById('open-glance')
const atAGlance = document.getElementById('at-a-glance')


// At a glance opening handler func
const openGlanceHandler = () => {
  atAGlance.classList.toggle('invisible')
}

// At a glance event listener
openAtAGlanceBtn.addEventListener('click', openGlanceHandler)
