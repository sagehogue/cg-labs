$('#submit').click(function (e) {
    console.log($('#toDoInput').val())
});
$('#toDoInput').keypress(function (e) {
    if (e.keyCode === 13) {
        attachListItem($(this).val())
    }
});

//ask chris for a study list of jS concepts that I could bang out over the weekend.
//I'm feeling a bit weak on the jS and it seems quite powerful if I can get it down so I should make sure to inquire.