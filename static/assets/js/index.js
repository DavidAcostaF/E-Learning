

function inputFile(){
    file = document.getElementById("file")
    file_text = document.getElementById("file_name")
    if(file.value){
        console.log(file.value)
        file_text.hidden = false
    }else{
        file_text.hidden = true
    }
}