$(document).ready(function() {
    var error_field = $(".errors");

    Array.from(error_field).forEach(function (item, i, arr) {
        var block_id = '#block-' + item.id.split('-')[1];
        $(block_id).addClass("has-error");
    });
});