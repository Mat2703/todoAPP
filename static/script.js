console.log('Script loaded successfully');

function showEditForm(taskId) {
    document.getElementById('editForm' + taskId).style.display = 'block';
}

function hideEditForm(taskId) {
    document.getElementById('editForm' + taskId).style.display = 'none';
}


