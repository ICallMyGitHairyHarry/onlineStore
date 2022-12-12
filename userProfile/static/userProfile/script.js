/* 1) удаляет из полей Фамилия и Имя служебные сиволы и цифры.
2) первую  букву введенного слова делает прописной. */
function correct_field(input_id){
    let input = document.getElementById(input_id).value
    input = input.replace(/[<>\.\/,\$0-9]/g, '');
    input = input.toLowerCase();
    input = FirstLetter(input);
    document.getElementById(input_id).value = input;
}

//Функция делает первую букву (в текстовой переменной str) прописной.
function FirstLetter(str){
    return str[0].toUpperCase() + str.substring(1);
}


