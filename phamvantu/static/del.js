$(document).ready(function() {
    $('.deleteButton').on('click', function(event) {

        var todo_id = $(this).attr('todo_id');
        //console.log($(event.target).closet('form'));
        var todo = $('#todoInput'+todo_id).val();
        var ngay = $('#ngayInput'+todo_id).val();
        // console.log(JSON.stringify({ todo : todo, ngay : ngay, id : todo_id }));

        req = $.ajax({
            url : '/api/todo',
            type : 'POST',
            data: JSON.stringify({id: todo_id}),
            contentType: 'application/json',
            dataType: 'json'
        }).done(function(data) {
            data = "Xoa thanh cong"
            alert(data)
        });
    

    });

});