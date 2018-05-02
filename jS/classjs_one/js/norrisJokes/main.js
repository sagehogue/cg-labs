function beJoking() {
    $.ajax({
        url: 'https://api.icndb.com/jokes/random',
        type: 'GET',
        success: function (response) {
            $('#jokeID').html(response.value.id);
            $('#joke').html(response.value.joke);
        }
    });
    // $('*').each(function() {
    //     this.style.backgroundColor
    // }) Ask how to making colors randomly change or somethin.

}

$('#new').click(function () {
   beJoking();
});
$(document).ready(function () {
    beJoking()
});