/**
 * Created by xinyue on 2016/12/12.
 */
KindEditor.ready(function(K) {
	editor = K.create('#id_content', {
		resizeType : 1,
        themeType : 'simple',
		items : [
			'source', 'preview', '|', 'undo', 'redo', '|','formatblock', 'fontname', 'fontsize','code', '|',
            'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',	'removeformat', '|', 'justifyleft',
            'justifycenter', 'justifyright', 'insertorderedlist', 'insertunorderedlist', '|',
            'emoticons', 'image', 'link', 'clearhtml'],
        uploadJson: '/admin/upload/kindeditor',
	});
});