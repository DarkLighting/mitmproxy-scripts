mitmproxy-scripts
=================

**Unofficial** scripts developed for use with the [mitmproxy](https://github.com/mitmproxy) project.
<br><br>

<h5>Features requests/issues are welcome!</h5>
<br>

<h4>Scripts list</h4>
*Obs: all scripts will write their outputs inside your current work folder (the one you were at when the mitmproxy tool was called), unless specified otherwise in this explanation.
<br>
<dl>
<dt>dump_headers.py
</dt>
<dd>Dumps the flow headers (with their respective values) inside the file "headers".
</dd>
<dt>dump_content.py
</dt>
<dd>Dumps the flow content in a file. It will create a directory called "content" and a subdirectorie for the content-type. Inside this folder it will put the content retrieved, in a file named after it's <i>sha1</i> hash and a part of the content-type.
<br><br>
Lets say you made a request and it returned a gif image. It's content-type will be "image/gif" and it has a sha1 hash of <i>"3d55ea361fc605f70ae51006b4e13b746cfe10f4"</i>. As you will see, the image will be created as <i>"content/image_gif/3d55ea361fc605f70ae51006b4e13b746cfe10f4_gif"</i>. 
<br>An HTML page with hash <i>"4a785571983375e723ec42e3748d6a0fdfa1716e"</i> would be created as <i>"content/text_html/4a785571983375e723ec42e3748d6a0fdfa1716e_html"</i>
</dd>
</dl>
