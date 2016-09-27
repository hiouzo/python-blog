KindEditor.ready(function(K) {
    K.create('textarea[name=content]',{
        width:'600px',
        height:'280px',
        uploadJson: '/admin/upload/kindeditor'
    });
});