
function deleteActivity(id){
    const modal = new bootstrap.Modal(document.getElementById('modal'))
    modal.show()
    form = document.getElementById('form_delete')
    form.action = `/classroom/delete_activity/${id}/`
}