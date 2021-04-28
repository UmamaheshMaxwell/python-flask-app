$(() => {
    $("#updateTask").click(() => {
        data = { 'content': $("#content").val() }
        $.ajax({
            url: `/update/${$("#taskId").val()}`,
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                window.location.href = window.location.href
            },
            error: function (error) {
                console.log(error);
            }
        });
    })
})

function edit_task(id) {
    $(function () {
        $.ajax({
            url: '/getTaskById/' + id,
            type: 'GET',
            success: function (data) {
                $("#content").val(data.content)
                $("#taskId").val(data.id)
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
}

