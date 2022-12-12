let basket = {};
let prices = {};

function get_items(items_amount, items_prices) {
    basket = items_amount;
    prices = items_prices;
}

function show_items() {
    for (let item in basket) {
        document.getElementById("amount" + item).innerText = basket[item];
        document.getElementById("price" + item).innerText = prices[item] + " P";
    }
}

function calc_full_price() {
    let full_price = 0;
    for (let price in prices) {
        full_price += prices[price]
    }
    document.getElementById("full_price").innerText = full_price + " P";
}

function add_item(pr_id, pr_price) {
    basket[pr_id] += 1;
    document.getElementById("amount" + pr_id).innerText = basket[pr_id];
    add_to_cart(pr_id);

    prices[pr_id] += pr_price;
    document.getElementById("price" + pr_id).innerText = prices[pr_id] + " P";
    calc_full_price();
}

function subtract_item(pr_id, pr_price) {
    basket[pr_id] -= 1;
    prices[pr_id] -= pr_price;
    if (basket[pr_id] === 0) {
        document.getElementById("pr_" + pr_id).classList.add("absent");
    } else {
        document.getElementById("amount" + pr_id).innerText = basket[pr_id];
        document.getElementById("price" + pr_id).innerText = prices[pr_id] + " P";
    }
    calc_full_price();
    subtract_from_cart(pr_id);
}

async function add_to_cart(pr_id) {
    await fetch(`/basket/add_product/${pr_id}`);
}

async function subtract_from_cart(pr_id) {
    await fetch(`/basket/subtract_product/${pr_id}`);
}

// order.html

/* 1) удаляет из полей служебные сиволы и цифры.
2) первую  букву введенного слова делает прописной. */
function correct_field(input_id){
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