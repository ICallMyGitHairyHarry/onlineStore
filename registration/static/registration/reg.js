// Функция сравнивает содержание введенных паролей.

let pass_message = document.getElementById("pass_message");
let conf_message = document.getElementById("conf_message");
let pass = document.getElementById("password");

function confirm_pass(){
    let conf = document.getElementById("password_conf");
        if(pass.value !== conf.value) {
            pass.focus();
            conf.value = ""
            conf_message.innerHTML = "Пароли не совпадают";
        } else {
            conf_message.innerHTML = "";
        }
}

/* Функция удаляет из первого поля с паролем служебные символы и Устанавливает ограничение
на минимальное количество символов (равное 7). */
function check_pass(){
    pass.value = pass.value.replace(/[<>/.//,/$]/g, '');
    let pass_length = pass.value.length;
    if (pass_length < 7) {
        pass.value = "";
        pass_message.innerHTML = "Количество символов в пароле должно быть больше 6";
    } else {
        pass_message.innerHTML = "";
    }
}

/* 1) удаляет из полей Фамилия и Имя служебные сиволы и цифры.
2) первую  букву введенного слова делает прописной. */
function correct_name(input_id){
    let input = document.getElementById(input_id).value
    input = input.replace(/[<>\.\/,\$0-9\s]/g, '');
    input = input.toLowerCase();
    input = FirstLetter(input);
    document.getElementById(input_id).value = input;
}

//Функция делает первую букву (в текстовой переменной str) прописной.
function FirstLetter(str){
    return str[0].toUpperCase() + str.substring(1);
}