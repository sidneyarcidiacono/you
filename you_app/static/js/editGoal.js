// Global constant to redirect to goal edit page
const openEditGoalBtn = document.querySelector('.open-edit-goal')

// Event listener for redirect to edit goal page
openEditGoalBtn.addEventListener('click', () => {
  window.location.href = '/edit_goal'
})
