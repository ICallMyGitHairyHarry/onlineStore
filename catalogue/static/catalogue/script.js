window.onscroll = function() {scrollEv()};
// window.onload = function() {scrollEv()};

// Get the navbar
const header = document.getElementById("hdr");

// Get the offset position of the navbar
const sticky = header.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function scrollEv() {
    if (window.pageYOffset >= sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

let basket = {};

function get_basket(session_items) {
    basket = session_items;
}

function show_number_buttons(id) {
    document.getElementById("pr_" + id).classList.add("absent");
    document.getElementById("pr_2_" + id).classList.remove("absent");
}

function hide_number_buttons(id) {
    document.getElementById("pr_" + id).classList.remove("absent");
    document.getElementById("pr_2_" + id).classList.add("absent");
}


function show_basket() {
    for (let item in basket) {
        show_number_buttons(item)
        document.getElementById("amount" + item).innerText = basket[item];
    }
}

function add_to_basket(pr_id) {
    show_number_buttons(pr_id)
    if (!(pr_id in basket)){
        basket[pr_id] = 1;
    } else {
        basket[pr_id] += 1;
    }
    add_to_cart(pr_id)
}

function add_pr(pr_id) {
    basket[pr_id] += 1;
    document.getElementById("amount" + pr_id).innerText = basket[pr_id];
    add_to_cart(pr_id)
}

function subtract_pr(pr_id) {
    basket[pr_id] -= 1;
    if (basket[pr_id] === 0) {
        hide_number_buttons(pr_id)
    } else {
        document.getElementById("amount" + pr_id).innerText = basket[pr_id];
    }
    subtract_from_cart(pr_id)
}

async function add_to_cart(pr_id) {
    await fetch(`/basket/add_product/${pr_id}`);
}

async function subtract_from_cart(pr_id) {
    await fetch(`/basket/subtract_product/${pr_id}`);
}

// product.html

let product_amount = 0

function get_amount(amount) {
    product_amount = amount;
}

function show_amount(id) {
    show_number_buttons(id);
    document.getElementById("amount" + id).innerText = product_amount;
}

function add_amount(pr_id) {
    product_amount += 1;
    document.getElementById("amount" + pr_id).innerText = product_amount;
    add_to_cart(pr_id)
}

function add_new_amount(pr_id) {
    product_amount += 1;
    show_number_buttons(pr_id);
    document.getElementById("amount" + pr_id).innerText = product_amount;
    add_to_cart(pr_id)
}

function subtract_amount(pr_id) {
    product_amount -= 1;
    if (product_amount === 0) {
        hide_number_buttons(pr_id)
    } else {
        document.getElementById("amount" + pr_id).innerText = product_amount;
    }
    subtract_from_cart(pr_id)
}

