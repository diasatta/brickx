from brickx.elements import *
from brickx.node import Element

class TestElementAttrs():
  def test_accesskey(self) -> None:
    assert Element(h_accesskey="foo").render_attrs() == 'accesskey="foo"'

  def test_autocapitalize(self) -> None:
    assert Element(h_autocapitalize="foo").render_attrs() == 'autocapitalize="foo"'

  def test_autofocus(self) -> None:
    assert Element(h_autofocus=True).render_attrs() == 'autofocus'

  def test_class_(self) -> None:
    assert Element(h_class="foo").render_attrs() == 'class="foo"'

  def test_contenteditable(self) -> None:
    assert Element(h_contenteditable="foo").render_attrs() == 'contenteditable="foo"'

  def test_dir(self) -> None:
    assert Element(h_dir="auto").render_attrs() == 'dir="auto"'

  def test_draggable(self) -> None:
    assert Element(h_draggable="false").render_attrs() == 'draggable="false"'

  def test_enterkeyhint(self) -> None:
    assert Element(h_enterkeyhint="foo").render_attrs() == 'enterkeyhint="foo"'

  def test_hidden(self) -> None:
    assert Element(h_hidden=True).render_attrs() == 'hidden'

  def test_id(self) -> None:
    assert Element(h_id="foo").render_attrs() == 'id="foo"'

  def test_inert(self) -> None:
    assert Element(h_inert=True).render_attrs() == 'inert'

  def test_inputmode(self) -> None:
    assert Element(h_inputmode="email").render_attrs() == 'inputmode="email"'

  def test_is_(self) -> None:
    assert Element(h_is="foo").render_attrs() == 'is="foo"'

  def test_itemid(self) -> None:
    assert Element(h_itemid="foo").render_attrs() == 'itemid="foo"'

  def test_itemprop(self) -> None:
    assert Element(h_itemprop="foo").render_attrs() == 'itemprop="foo"'

  def test_itemref(self) -> None:
    assert Element(h_itemref="foo").render_attrs() == 'itemref="foo"'

  def test_itemscope(self) -> None:
    assert Element(h_itemscope=True).render_attrs() == 'itemscope'

  def test_itemtype(self) -> None:
    assert Element(h_itemtype='www.foo.bar/baz/?quux="1"').render_attrs() == 'itemtype="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_lang(self) -> None:
    assert Element(h_lang="foo").render_attrs() == 'lang="foo"'

  def test_nonce(self) -> None:
    assert Element(h_nonce="foo").render_attrs() == 'nonce="foo"'

  def test_part(self) -> None:
    assert Element(h_part="foo").render_attrs() == 'part="foo"'

  def test_popover(self) -> None:
    assert Element(h_popover="foo").render_attrs() == 'popover="foo"'

  def test_role(self) -> None:
    assert Element(h_role="alert").render_attrs() == 'role="alert"'

  def test_slot(self) -> None:
    assert Element(h_slot="foo").render_attrs() == 'slot="foo"'

  def test_spellcheck(self) -> None:
    assert Element(h_spellcheck="false").render_attrs() == 'spellcheck="false"'

  def test_style(self) -> None:
    assert Element(h_style="width: 1px;").render_attrs() == 'style="width: 1px;"'

  def test_tabindex(self) -> None:
    assert Element(h_tabindex="foo").render_attrs() == 'tabindex="foo"'

  def test_title(self) -> None:
    assert Element(h_title="foo").render_attrs() == 'title="foo"'

  def test_translate(self) -> None:
    assert Element(h_translate="no").render_attrs() == 'translate="no"'

  def test_virtualkeyboardpolicy(self) -> None:
    assert Element(h_virtualkeyboardpolicy="foo").render_attrs() == 'virtualkeyboardpolicy="foo"'

class TestAAttrs():
  def test_download(self) -> None:
    assert A(h_download="foo").render_attrs() == 'download="foo"'

  def test_href(self) -> None:
    assert A(h_href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_hreflang(self) -> None:
    assert A(h_hreflang="foo").render_attrs() == 'hreflang="foo"'

  def test_ping(self) -> None:
    assert A(h_ping='www.foo.bar/baz/?quux="1"').render_attrs() == 'ping="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_referrerpolicy(self) -> None:
    assert A(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert A(h_rel="alternate").render_attrs() == 'rel="alternate"'

  def test_target(self) -> None:
    assert A(h_target="_blank").render_attrs() == 'target="_blank"'

  def test_type(self) -> None:
    assert A(h_type="foo").render_attrs() == 'type="foo"'

class TestAreaAttrs():
  def test_alt(self) -> None:
    assert Area(h_alt="foo").render_attrs() == 'alt="foo"'

  def test_coords(self) -> None:
    assert Area(h_coords="foo").render_attrs() == 'coords="foo"'

  def test_download(self) -> None:
    assert Area(h_download="foo").render_attrs() == 'download="foo"'

  def test_href(self) -> None:
    assert Area(h_href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_ping(self) -> None:
    assert Area(h_ping='www.foo.bar/baz/?quux="1"').render_attrs() == 'ping="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_referrerpolicy(self) -> None:
    assert Area(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert Area(h_rel="alternate").render_attrs() == 'rel="alternate"'

  def test_shape(self) -> None:
    assert Area(h_shape="circle").render_attrs() == 'shape="circle"'

  def test_target(self) -> None:
    assert Area(h_target="_blank").render_attrs() == 'target="_blank"'

class TestAudioAttrs():
  def test_autoplay(self) -> None:
    assert Audio(h_autoplay=True).render_attrs() == 'autoplay'

  def test_controls(self) -> None:
    assert Audio(h_controls=True).render_attrs() == 'controls'

  def test_crossorigin(self) -> None:
    assert Audio(h_crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_loop(self) -> None:
    assert Audio(h_loop=True).render_attrs() == 'loop'

  def test_muted(self) -> None:
    assert Audio(h_muted=True).render_attrs() == 'muted'

  def test_preload(self) -> None:
    assert Audio(h_preload="auto").render_attrs() == 'preload="auto"'

  def test_src(self) -> None:
    assert Audio(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestBaseAttrs():
  def test_href(self) -> None:
    assert Base(h_href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_target(self) -> None:
    assert Base(h_target="_blank").render_attrs() == 'target="_blank"'

class TestBlockquoteAttrs():
  def test_cite(self) -> None:
    assert Blockquote(h_cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestBodyAttrs():
  def test_onafterprint(self) -> None:
    assert Body(h_onafterprint="foo()").render_attrs() == 'onafterprint="foo()"'

  def test_onbeforeprint(self) -> None:
    assert Body(h_onbeforeprint="foo()").render_attrs() == 'onbeforeprint="foo()"'

  def test_onbeforeunload(self) -> None:
    assert Body(h_onbeforeunload="foo()").render_attrs() == 'onbeforeunload="foo()"'

  def test_onblur(self) -> None:
    assert Body(h_onblur="foo()").render_attrs() == 'onblur="foo()"'

  def test_onerror(self) -> None:
    assert Body(h_onerror="foo()").render_attrs() == 'onerror="foo()"'

  def test_onfocus(self) -> None:
    assert Body(h_onfocus="foo()").render_attrs() == 'onfocus="foo()"'

  def test_onhashchange(self) -> None:
    assert Body(h_onhashchange="foo()").render_attrs() == 'onhashchange="foo()"'

  def test_onlanguagechange(self) -> None:
    assert Body(h_onlanguagechange="foo()").render_attrs() == 'onlanguagechange="foo()"'

  def test_onload(self) -> None:
    assert Body(h_onload="foo()").render_attrs() == 'onload="foo()"'

  def test_onmessage(self) -> None:
    assert Body(h_onmessage="foo()").render_attrs() == 'onmessage="foo()"'

  def test_onoffline(self) -> None:
    assert Body(h_onoffline="foo()").render_attrs() == 'onoffline="foo()"'

  def test_ononline(self) -> None:
    assert Body(h_ononline="foo()").render_attrs() == 'ononline="foo()"'

  def test_onpopstate(self) -> None:
    assert Body(h_onpopstate="foo()").render_attrs() == 'onpopstate="foo()"'

  def test_onredo(self) -> None:
    assert Body(h_onredo="foo()").render_attrs() == 'onredo="foo()"'

  def test_onresize(self) -> None:
    assert Body(h_onresize="foo()").render_attrs() == 'onresize="foo()"'

  def test_onstorage(self) -> None:
    assert Body(h_onstorage="foo()").render_attrs() == 'onstorage="foo()"'

  def test_onundo(self) -> None:
    assert Body(h_onundo="foo()").render_attrs() == 'onundo="foo()"'

  def test_onunload(self) -> None:
    assert Body(h_onunload="foo()").render_attrs() == 'onunload="foo()"'

class TestButtonAttrs():
  def test_autofocus(self) -> None:
    assert Button(h_autofocus=True).render_attrs() == 'autofocus'

  def test_disabled(self) -> None:
    assert Button(h_disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Button(h_form="foo").render_attrs() == 'form="foo"'

  def test_formaction(self) -> None:
    assert Button(h_formaction='www.foo.bar/baz/?quux="1"').render_attrs() == 'formaction="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_formenctype(self) -> None:
    assert Button(h_formenctype="application/x-www-form-urlencoded").render_attrs() == 'formenctype="application/x-www-form-urlencoded"'

  def test_formmethod(self) -> None:
    assert Button(h_formmethod="get").render_attrs() == 'formmethod="get"'

  def test_formnovalidate(self) -> None:
    assert Button(h_formnovalidate=True).render_attrs() == 'formnovalidate'

  def test_formtarget(self) -> None:
    assert Button(h_formtarget="_blank").render_attrs() == 'formtarget="_blank"'

  def test_name(self) -> None:
    assert Button(h_name="foo").render_attrs() == 'name="foo"'

  def test_type(self) -> None:
    assert Button(h_type="button").render_attrs() == 'type="button"'

  def test_value(self) -> None:
    assert Button(h_value="foo").render_attrs() == 'value="foo"'

class TestCanvasAttrs():
  def test_height(self) -> None:
    assert Canvas(h_height="foo").render_attrs() == 'height="foo"'

  def test_width(self) -> None:
    assert Canvas(h_width="foo").render_attrs() == 'width="foo"'

class TestColAttrs():
  def test_span(self) -> None:
    assert Col(h_span="foo").render_attrs() == 'span="foo"'

class TestColgroupAttrs():
  def test_span(self) -> None:
    assert Colgroup(h_span="foo").render_attrs() == 'span="foo"'

class TestDataAttrs():
  def test_value(self) -> None:
    assert Data(h_value="foo").render_attrs() == 'value="foo"'

class TestDelAttrs():
  def test_cite(self) -> None:
    assert Del(h_cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_datetime(self) -> None:
    assert Del(h_datetime="foo").render_attrs() == 'datetime="foo"'

class TestDetailsAttrs():
  def test_open(self) -> None:
    assert Details(h_open=True).render_attrs() == 'open'

class TestDialogAttrs():
  def test_open(self) -> None:
    assert Dialog(h_open=True).render_attrs() == 'open'

class TestEmbedAttrs():
  def test_height(self) -> None:
    assert Embed(h_height="foo").render_attrs() == 'height="foo"'

  def test_src(self) -> None:
    assert Embed(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Embed(h_type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Embed(h_width="foo").render_attrs() == 'width="foo"'

class TestFieldsetAttrs():
  def test_disabled(self) -> None:
    assert Fieldset(h_disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Fieldset(h_form="foo").render_attrs() == 'form="foo"'

  def test_name(self) -> None:
    assert Fieldset(h_name="foo").render_attrs() == 'name="foo"'

class TestFormAttrs():
  def test_accept_charset(self) -> None:
    assert Form(h_accept_charset="foo").render_attrs() == 'accept-charset="foo"'

  def test_action(self) -> None:
    assert Form(h_action='www.foo.bar/baz/?quux="1"').render_attrs() == 'action="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_autocomplete(self) -> None:
    assert Form(h_autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_enctype(self) -> None:
    assert Form(h_enctype="application/x-www-form-urlencoded").render_attrs() == 'enctype="application/x-www-form-urlencoded"'

  def test_method(self) -> None:
    assert Form(h_method="get").render_attrs() == 'method="get"'

  def test_name(self) -> None:
    assert Form(h_name="foo").render_attrs() == 'name="foo"'

  def test_novalidate(self) -> None:
    assert Form(h_novalidate=True).render_attrs() == 'novalidate'

  def test_rel(self) -> None:
    assert Form(h_rel="alternate").render_attrs() == 'rel="alternate"'

  def test_target(self) -> None:
    assert Form(h_target="_blank").render_attrs() == 'target="_blank"'

class TestHtmlAttrs():
  def test_xmlns(self) -> None:
    assert Html(h_xmlns='http://www.w3.org/1999/xhtml').render_attrs() == 'xmlns="http://www.w3.org/1999/xhtml"'

class TestIframeAttrs():
  def test_allow(self) -> None:
    assert Iframe(h_allow="foo").render_attrs() == 'allow="foo"'

  def test_allowfullscreen(self) -> None:
    assert Iframe(h_allowfullscreen="false").render_attrs() == 'allowfullscreen="false"'

  def test_height(self) -> None:
    assert Iframe(h_height="foo").render_attrs() == 'height="foo"'

  def test_loading(self) -> None:
    assert Iframe(h_loading="eager").render_attrs() == 'loading="eager"'

  def test_name(self) -> None:
    assert Iframe(h_name="foo").render_attrs() == 'name="foo"'

  def test_referrerpolicy(self) -> None:
    assert Iframe(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_sandbox(self) -> None:
    assert Iframe(h_sandbox="allow-forms").render_attrs() == 'sandbox="allow-forms"'

  def test_src(self) -> None:
    assert Iframe(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcdoc(self) -> None:
    assert Iframe(h_srcdoc='<foo class="bar"></foo>').render_attrs() == 'srcdoc="&lt;foo class=&quot;bar&quot;&gt;&lt;/foo&gt;"'

  def test_width(self) -> None:
    assert Iframe(h_width="foo").render_attrs() == 'width="foo"'

class TestImgAttrs():
  def test_alt(self) -> None:
    assert Img(h_alt="foo").render_attrs() == 'alt="foo"'

  def test_crossorigin(self) -> None:
    assert Img(h_crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_decoding(self) -> None:
    assert Img(h_decoding="async").render_attrs() == 'decoding="async"'

  def test_fetchpriority(self) -> None:
    assert Img(h_fetchpriority="auto").render_attrs() == 'fetchpriority="auto"'

  def test_height(self) -> None:
    assert Img(h_height="foo").render_attrs() == 'height="foo"'

  def test_ismap(self) -> None:
    assert Img(h_ismap=True).render_attrs() == 'ismap'

  def test_loading(self) -> None:
    assert Img(h_loading="eager").render_attrs() == 'loading="eager"'

  def test_referrerpolicy(self) -> None:
    assert Img(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_sizes(self) -> None:
    assert Img(h_sizes="foo").render_attrs() == 'sizes="foo"'

  def test_src(self) -> None:
    assert Img(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcset(self) -> None:
    assert Img(h_srcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'srcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_usemap(self) -> None:
    assert Img(h_usemap='www.foo.bar/baz/?quux="1"').render_attrs() == 'usemap="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_width(self) -> None:
    assert Img(h_width="foo").render_attrs() == 'width="foo"'

class TestInputAttrs():
  def test_accept(self) -> None:
    assert Input(h_accept="audio/*").render_attrs() == 'accept="audio/*"'

  def test_alt(self) -> None:
    assert Input(h_alt="foo").render_attrs() == 'alt="foo"'

  def test_autocomplete(self) -> None:
    assert Input(h_autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Input(h_autofocus=True).render_attrs() == 'autofocus'

  def test_capture(self) -> None:
    assert Input(h_capture="foo").render_attrs() == 'capture="foo"'

  def test_checked(self) -> None:
    assert Input(h_checked=True).render_attrs() == 'checked'

  def test_dirname(self) -> None:
    assert Input(h_dirname="foo").render_attrs() == 'dirname="foo"'

  def test_disabled(self) -> None:
    assert Input(h_disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Input(h_form="foo").render_attrs() == 'form="foo"'

  def test_formaction(self) -> None:
    assert Input(h_formaction='www.foo.bar/baz/?quux="1"').render_attrs() == 'formaction="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_formenctype(self) -> None:
    assert Input(h_formenctype="application/x-www-form-urlencoded").render_attrs() == 'formenctype="application/x-www-form-urlencoded"'

  def test_formmethod(self) -> None:
    assert Input(h_formmethod="get").render_attrs() == 'formmethod="get"'

  def test_formnovalidate(self) -> None:
    assert Input(h_formnovalidate=True).render_attrs() == 'formnovalidate'

  def test_formtarget(self) -> None:
    assert Input(h_formtarget="_blank").render_attrs() == 'formtarget="_blank"'

  def test_height(self) -> None:
    assert Input(h_height="foo").render_attrs() == 'height="foo"'

  def test_list(self) -> None:
    assert Input(h_list="foo").render_attrs() == 'list="foo"'

  def test_max(self) -> None:
    assert Input(h_max="foo").render_attrs() == 'max="foo"'

  def test_maxlength(self) -> None:
    assert Input(h_maxlength="foo").render_attrs() == 'maxlength="foo"'

  def test_min(self) -> None:
    assert Input(h_min="foo").render_attrs() == 'min="foo"'

  def test_minlength(self) -> None:
    assert Input(h_minlength="foo").render_attrs() == 'minlength="foo"'

  def test_multiple(self) -> None:
    assert Input(h_multiple=True).render_attrs() == 'multiple'

  def test_name(self) -> None:
    assert Input(h_name="foo").render_attrs() == 'name="foo"'

  def test_pattern(self) -> None:
    assert Input(h_pattern="foo").render_attrs() == 'pattern="foo"'

  def test_placeholder(self) -> None:
    assert Input(h_placeholder="foo").render_attrs() == 'placeholder="foo"'

  def test_readonly(self) -> None:
    assert Input(h_readonly=True).render_attrs() == 'readonly'

  def test_required(self) -> None:
    assert Input(h_required=True).render_attrs() == 'required'

  def test_size(self) -> None:
    assert Input(h_size="foo").render_attrs() == 'size="foo"'

  def test_src(self) -> None:
    assert Input(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_step(self) -> None:
    assert Input(h_step="foo").render_attrs() == 'step="foo"'

  def test_type(self) -> None:
    assert Input(h_type="button").render_attrs() == 'type="button"'

  def test_value(self) -> None:
    assert Input(h_value="foo").render_attrs() == 'value="foo"'

  def test_width(self) -> None:
    assert Input(h_width="foo").render_attrs() == 'width="foo"'

class TestInsAttrs():
  def test_cite(self) -> None:
    assert Ins(h_cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_datetime(self) -> None:
    assert Ins(h_datetime="foo").render_attrs() == 'datetime="foo"'

class TestLabelAttrs():
  def test_for_(self) -> None:
    assert Label(h_for="foo").render_attrs() == 'for="foo"'

class TestLiAttrs():
  def test_value(self) -> None:
    assert Li(h_value="foo").render_attrs() == 'value="foo"'

class TestLinkAttrs():
  def test_as_(self) -> None:
    assert Link(h_as="foo").render_attrs() == 'as="foo"'

  def test_crossorigin(self) -> None:
    assert Link(h_crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_fetchpriority(self) -> None:
    assert Link(h_fetchpriority="foo").render_attrs() == 'fetchpriority="foo"'

  def test_href(self) -> None:
    assert Link(h_href='www.foo.bar/baz/?quux="1"').render_attrs() == 'href="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_hreflang(self) -> None:
    assert Link(h_hreflang="foo").render_attrs() == 'hreflang="foo"'

  def test_imagesizes(self) -> None:
    assert Link(h_imagesizes="foo").render_attrs() == 'imagesizes="foo"'

  def test_imagesrcset(self) -> None:
    assert Link(h_imagesrcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'imagesrcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_integrity(self) -> None:
    assert Link(h_integrity="foo").render_attrs() == 'integrity="foo"'

  def test_media(self) -> None:
    assert Link(h_media="foo").render_attrs() == 'media="foo"'

  def test_referrerpolicy(self) -> None:
    assert Link(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_rel(self) -> None:
    assert Link(h_rel="alternate").render_attrs() == 'rel="alternate"'

  def test_sizes(self) -> None:
    assert Link(h_sizes="foo").render_attrs() == 'sizes="foo"'

  def test_type(self) -> None:
    assert Link(h_type="foo").render_attrs() == 'type="foo"'

class TestMapAttrs():
  def test_name(self) -> None:
    assert Map(h_name="foo").render_attrs() == 'name="foo"'

class TestMetaAttrs():
  def test_charset(self) -> None:
    assert Meta(h_charset="foo").render_attrs() == 'charset="foo"'

  def test_content(self) -> None:
    assert Meta(h_content="foo").render_attrs() == 'content="foo"'

  def test_http_equiv(self) -> None:
    assert Meta(h_http_equiv="content-security-policy").render_attrs() == 'http-equiv="content-security-policy"'

  def test_name(self) -> None:
    assert Meta(h_name="application-name").render_attrs() == 'name="application-name"'

class TestMeterAttrs():
  def test_form(self) -> None:
    assert Meter(h_form="foo").render_attrs() == 'form="foo"'

  def test_high(self) -> None:
    assert Meter(h_high="foo").render_attrs() == 'high="foo"'

  def test_low(self) -> None:
    assert Meter(h_low="foo").render_attrs() == 'low="foo"'

  def test_max(self) -> None:
    assert Meter(h_max="foo").render_attrs() == 'max="foo"'

  def test_min(self) -> None:
    assert Meter(h_min="foo").render_attrs() == 'min="foo"'

  def test_optimum(self) -> None:
    assert Meter(h_optimum="foo").render_attrs() == 'optimum="foo"'

  def test_value(self) -> None:
    assert Meter(h_value="foo").render_attrs() == 'value="foo"'

class TestObjectAttrs():
  def test_data(self) -> None:
    assert Object(h_data='www.foo.bar/baz/?quux="1"').render_attrs() == 'data="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_form(self) -> None:
    assert Object(h_form="foo").render_attrs() == 'form="foo"'

  def test_height(self) -> None:
    assert Object(h_height="foo").render_attrs() == 'height="foo"'

  def test_name(self) -> None:
    assert Object(h_name="foo").render_attrs() == 'name="foo"'

  def test_type(self) -> None:
    assert Object(h_type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Object(h_width="foo").render_attrs() == 'width="foo"'

class TestOlAttrs():
  def test_reversed(self) -> None:
    assert Ol(h_reversed=True).render_attrs() == 'reversed'

  def test_start(self) -> None:
    assert Ol(h_start="foo").render_attrs() == 'start="foo"'

  def test_type(self) -> None:
    assert Ol(h_type="1").render_attrs() == 'type="1"'

class TestOptgroupAttrs():
  def test_disabled(self) -> None:
    assert Optgroup(h_disabled=True).render_attrs() == 'disabled'

  def test_label(self) -> None:
    assert Optgroup(h_label="foo").render_attrs() == 'label="foo"'

class TestOptionAttrs():
  def test_disabled(self) -> None:
    assert Option(h_disabled=True).render_attrs() == 'disabled'

  def test_label(self) -> None:
    assert Option(h_label="foo").render_attrs() == 'label="foo"'

  def test_selected(self) -> None:
    assert Option(h_selected=True).render_attrs() == 'selected'

  def test_value(self) -> None:
    assert Option(h_value="foo").render_attrs() == 'value="foo"'

class TestOutputAttrs():
  def test_for_(self) -> None:
    assert Output(h_for="foo").render_attrs() == 'for="foo"'

  def test_form(self) -> None:
    assert Output(h_form="foo").render_attrs() == 'form="foo"'

  def test_name(self) -> None:
    assert Output(h_name="foo").render_attrs() == 'name="foo"'

class TestProgressAttrs():
  def test_max(self) -> None:
    assert Progress(h_max="foo").render_attrs() == 'max="foo"'

  def test_value(self) -> None:
    assert Progress(h_value="foo").render_attrs() == 'value="foo"'

class TestQAttrs():
  def test_cite(self) -> None:
    assert Q(h_cite='www.foo.bar/baz/?quux="1"').render_attrs() == 'cite="www.foo.bar/baz/?quux=&quot;1&quot;"'

class TestScriptAttrs():
  def test_async_(self) -> None:
    assert Script(h_async=True).render_attrs() == 'async'

  def test_crossorigin(self) -> None:
    assert Script(h_crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_defer(self) -> None:
    assert Script(h_defer=True).render_attrs() == 'defer'

  def test_fetchpriority(self) -> None:
    assert Script(h_fetchpriority="foo").render_attrs() == 'fetchpriority="foo"'

  def test_integrity(self) -> None:
    assert Script(h_integrity="foo").render_attrs() == 'integrity="foo"'

  def test_nomodule(self) -> None:
    assert Script(h_nomodule=True).render_attrs() == 'nomodule'

  def test_nonce(self) -> None:
    assert Script(h_nonce="foo").render_attrs() == 'nonce="foo"'

  def test_referrerpolicy(self) -> None:
    assert Script(h_referrerpolicy="no-referrer").render_attrs() == 'referrerpolicy="no-referrer"'

  def test_src(self) -> None:
    assert Script(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Script(h_type="foo").render_attrs() == 'type="foo"'

class TestSelectAttrs():
  def test_autocomplete(self) -> None:
    assert Select(h_autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Select(h_autofocus=True).render_attrs() == 'autofocus'

  def test_disabled(self) -> None:
    assert Select(h_disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Select(h_form="foo").render_attrs() == 'form="foo"'

  def test_multiple(self) -> None:
    assert Select(h_multiple=True).render_attrs() == 'multiple'

  def test_name(self) -> None:
    assert Select(h_name="foo").render_attrs() == 'name="foo"'

  def test_required(self) -> None:
    assert Select(h_required=True).render_attrs() == 'required'

  def test_size(self) -> None:
    assert Select(h_size="foo").render_attrs() == 'size="foo"'

class TestSlotAttrs():
  def test_name(self) -> None:
    assert Slot(h_name="foo").render_attrs() == 'name="foo"'

class TestSourceAttrs():
  def test_height(self) -> None:
    assert Source(h_height="foo").render_attrs() == 'height="foo"'

  def test_media(self) -> None:
    assert Source(h_media="foo").render_attrs() == 'media="foo"'

  def test_sizes(self) -> None:
    assert Source(h_sizes="foo").render_attrs() == 'sizes="foo"'

  def test_src(self) -> None:
    assert Source(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srcset(self) -> None:
    assert Source(h_srcset='www.foo.bar/baz/?quux="1"').render_attrs() == 'srcset="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_type(self) -> None:
    assert Source(h_type="foo").render_attrs() == 'type="foo"'

  def test_width(self) -> None:
    assert Source(h_width="foo").render_attrs() == 'width="foo"'

class TestStyleAttrs():
  def test_blocking(self) -> None:
    assert Style(h_blocking="foo").render_attrs() == 'blocking="foo"'

  def test_media(self) -> None:
    assert Style(h_media="foo").render_attrs() == 'media="foo"'

  def test_nonce(self) -> None:
    assert Style(h_nonce="foo").render_attrs() == 'nonce="foo"'

  def test_title(self) -> None:
    assert Style(h_title="foo").render_attrs() == 'title="foo"'

class TestTdAttrs():
  def test_colspan(self) -> None:
    assert Td(h_colspan="foo").render_attrs() == 'colspan="foo"'

  def test_headers(self) -> None:
    assert Td(h_headers="foo").render_attrs() == 'headers="foo"'

  def test_rowspan(self) -> None:
    assert Td(h_rowspan="foo").render_attrs() == 'rowspan="foo"'

class TestTextareaAttrs():
  def test_autocomplete(self) -> None:
    assert Textarea(h_autocomplete="additional-name").render_attrs() == 'autocomplete="additional-name"'

  def test_autofocus(self) -> None:
    assert Textarea(h_autofocus=True).render_attrs() == 'autofocus'

  def test_cols(self) -> None:
    assert Textarea(h_cols="foo").render_attrs() == 'cols="foo"'

  def test_dirname(self) -> None:
    assert Textarea(h_dirname="foo").render_attrs() == 'dirname="foo"'

  def test_disabled(self) -> None:
    assert Textarea(h_disabled=True).render_attrs() == 'disabled'

  def test_form(self) -> None:
    assert Textarea(h_form="foo").render_attrs() == 'form="foo"'

  def test_maxlength(self) -> None:
    assert Textarea(h_maxlength="foo").render_attrs() == 'maxlength="foo"'

  def test_minlength(self) -> None:
    assert Textarea(h_minlength="foo").render_attrs() == 'minlength="foo"'

  def test_name(self) -> None:
    assert Textarea(h_name="foo").render_attrs() == 'name="foo"'

  def test_placeholder(self) -> None:
    assert Textarea(h_placeholder="foo").render_attrs() == 'placeholder="foo"'

  def test_readonly(self) -> None:
    assert Textarea(h_readonly=True).render_attrs() == 'readonly'

  def test_required(self) -> None:
    assert Textarea(h_required=True).render_attrs() == 'required'

  def test_rows(self) -> None:
    assert Textarea(h_rows="foo").render_attrs() == 'rows="foo"'

  # def test_spellcheck(self) -> None:
  #   assert Textarea(h_spellcheck="default").render_attrs() == 'spellcheck="default"'

  def test_wrap(self) -> None:
    assert Textarea(h_wrap="hard").render_attrs() == 'wrap="hard"'

class TestThAttrs():
  def test_abbr(self) -> None:
    assert Th(h_abbr="foo").render_attrs() == 'abbr="foo"'

  def test_colspan(self) -> None:
    assert Th(h_colspan="foo").render_attrs() == 'colspan="foo"'

  def test_headers(self) -> None:
    assert Th(h_headers="foo").render_attrs() == 'headers="foo"'

  def test_rowspan(self) -> None:
    assert Th(h_rowspan="foo").render_attrs() == 'rowspan="foo"'

  def test_scope(self) -> None:
    assert Th(h_scope="col").render_attrs() == 'scope="col"'

class TestTimeAttrs():
  def test_datetime(self) -> None:
    assert Time(h_datetime="foo").render_attrs() == 'datetime="foo"'

class TestTrackAttrs():
  def test_default(self) -> None:
    assert Track(h_default=True).render_attrs() == 'default'

  def test_kind(self) -> None:
    assert Track(h_kind="captions").render_attrs() == 'kind="captions"'

  def test_label(self) -> None:
    assert Track(h_label="foo").render_attrs() == 'label="foo"'

  def test_src(self) -> None:
    assert Track(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_srclang(self) -> None:
    assert Track(h_srclang="foo").render_attrs() == 'srclang="foo"'

class TestVideoAttrs():
  def test_autoplay(self) -> None:
    assert Video(h_autoplay=True).render_attrs() == 'autoplay'

  def test_controls(self) -> None:
    assert Video(h_controls=True).render_attrs() == 'controls'

  def test_crossorigin(self) -> None:
    assert Video(h_crossorigin="anonymous").render_attrs() == 'crossorigin="anonymous"'

  def test_disableremoteplayback(self) -> None:
    assert Video(h_disableremoteplayback=True).render_attrs() == 'disableremoteplayback'

  def test_loop(self) -> None:
    assert Video(h_loop=True).render_attrs() == 'loop'

  def test_muted(self) -> None:
    assert Video(h_muted=True).render_attrs() == 'muted'

  def test_playsinline(self) -> None:
    assert Video(h_playsinline=True).render_attrs() == 'playsinline'

  def test_poster(self) -> None:
    assert Video(h_poster='www.foo.bar/baz/?quux="1"').render_attrs() == 'poster="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_preload(self) -> None:
    assert Video(h_preload="auto").render_attrs() == 'preload="auto"'

  def test_src(self) -> None:
    assert Video(h_src='www.foo.bar/baz/?quux="1"').render_attrs() == 'src="www.foo.bar/baz/?quux=&quot;1&quot;"'

  def test_width(self) -> None:
    assert Video(h_width="foo").render_attrs() == 'width="foo"'

