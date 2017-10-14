/**
 * Created by xinyue on 2016/12/12.
 */
KindEditor.ready(function (K) {
    editor = K.create('#id_content', {
        resizeType: 1,
        width: '1000px',
        height: '500px',
        themeType: 'simple',
        items: [
            'source', 'preview', '|', 'undo', 'redo', '|', 'formatblock', 'fontname', 'fontsize', 'code', '|',
            'forecolor', 'hilitecolor', 'bold', 'italic', 'underline', 'removeformat', '|', 'justifyleft',
            'justifycenter', 'justifyright', 'insertorderedlist', 'insertunorderedlist', '|',
            'emoticons', 'image', 'link', 'clearhtml'],
        uploadJson: '/admin/upload/kindeditor',
    });
});