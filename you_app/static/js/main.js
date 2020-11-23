const openAtAGlanceBtn = document.getElementById('open-glance')
const atAGlance = document.getElementById('at-a-glance')

const openGlanceHandler = () => {
  atAGlance.classList.toggle('invisible')
}

openAtAGlanceBtn.addEventListener('click', openGlanceHandler)
