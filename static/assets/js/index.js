
function deleteActivity(id){
    const modal = new bootstrap.Modal(document.getElementById('modal'))
    modal.show()
    form = document.getElementById('form_delete')
    form.action = `/classroom/delete_activity/${id}/`
}

function cancelGrade(id){
    const modal = new bootstrap.Modal(document.getElementById('modal_cancel'))
    modal.show()
    form = document.getElementById('cancel_grade')
    form.action = `/classroom/submited_files/cancel_grade/${id}/`
}