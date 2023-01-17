"use strict";

window.onload = function () {
    console.log("DOM ready");
    $('.basket_list').on('change', 'input[type=number]', function (event) {
        $.ajax({
            url: "/basket/set/" + event.target.name + "/" + event.target.value + "/",
            success: function (answer) {
                document.querySelector('.basket_list').innerHTML = answer.basket_list;
            }
        });
    })
    // 7 min -> 20:08 AIR
    // let categoryNames = document.querySelectorAll('input[type=number]');
    // categoryNames.forEach(function (item) {
    //     item.onchange = function (event) {
    //         let qty = event.target.value
    //         let pk = event.target.name
    //         console.log("qty:" + qty + ", pk " + pk);
    //         $.ajax({
    //             url: "/basket/set/" + pk + "/" + qty + "/",
    //             success: function (answer) {
    //                 console.log("answer", answer);
    //                 // refresh  basket item, refresh basket stat
    //                 document.querySelector('.basket_list').innerHTML = answer.basket_list;
    //             }
    //         });
    //     }
    // })
}
