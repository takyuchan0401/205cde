
function validateForm() {
    var pizza1 = document.forms["checkoutForm"]["pizza1"].value;
    var pizza2 = document.forms["checkoutForm"]["pizza2"].value;
    var pizza3 = document.forms["checkoutForm"]["pizza3"].value;
    var pizza4 = document.forms["checkoutForm"]["pizza4"].value;
    var pizza5 = document.forms["checkoutForm"]["pizza5"].value;
    var pizza6 = document.forms["checkoutForm"]["pizza6"].value;
    var pizza1size = document.forms["checkoutForm"]["pizza1size"].value;
    var pizza2size = document.forms["checkoutForm"]["pizza2size"].value;
    var pizza3size = document.forms["checkoutForm"]["pizza3size"].value;
    var pizza4size = document.forms["checkoutForm"]["pizza4size"].value;
    var pizza5size = document.forms["checkoutForm"]["pizza5size"].value;
    var pizza6size = document.forms["checkoutForm"]["pizza6size"].value;

    if (pizza1 == 0 & pizza2 == 0 & pizza3 == 0 & pizza4 == 0 & pizza5 == 0 & pizza6 == 0) {
        alert("Please add an item to the cart to checkout");
        return false;
    }
    
    if (pizza1 != 0 & pizza1size == "Size"){
        alert("Please select size for the pepporoni pizza");
        return false;
    }

    if (pizza2 != 0 & pizza2size == "Size"){
        alert("Please select size for the 2 pizza");
        return false;
    }

    if (pizza3 != 0 & pizza3size == "Size"){
        alert("Please select size for the 3 pizza");
        return false;
    }

    if (pizza4 != 0 & pizza4size == "Size"){
        alert("Please select size for the 4 pizza");
        return false;
    }

    if (pizza5 != 0 & pizza5size == "Size"){
        alert("Please select size for the 5 pizza");
        return false;
    }

    if (pizza6 != 0 & pizza6size == "Size"){
        alert("Please select size for the 6 pizza");
        return false;
    }
}