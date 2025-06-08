from typing import Literal

#region Attribute Literals
AReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
ARelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
ATargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
AreaReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
AreaRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
AreaShapeL = Literal[
  "circle",
  "default",
  "poly",
  "rect",
]
AreaTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
AudioCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
AudioPreloadL = Literal[
  "auto",
  "metadata",
  "none",
]
BaseTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
ButtonFormenctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
ButtonFormmethodL = Literal[
  "get",
  "post",
]
ButtonFormtargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
ButtonTypeL = Literal[
  "button",
  "reset",
  "submit",
]
DirL = Literal[
  "auto",
  "ltr",
  "rtl",
]
DraggableL = Literal[
  "false",
  "true",
]
FormAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
FormEnctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
FormMethodL = Literal[
  "get",
  "post",
]
FormRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
FormTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
HtmlXmlnsL = Literal[
  "http://www.w3.org/1999/xhtml",
]
IframeAllowfullscreenL = Literal[
  "false",
  "true",
]
IframeLoadingL = Literal[
  "eager",
  "lazy",
]
IframeReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
IframeSandboxL = Literal[
  "allow-forms",
  "allow-pointer-lock",
  "allow-popups",
  "allow-same-origin",
  "allow-scripts",
  "allow-top-navigation",
]
ImgCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
ImgDecodingL = Literal[
  "async",
  "auto",
  "sync",
]
ImgFetchpriorityL = Literal[
  "auto",
  "high",
  "low",
]
ImgLoadingL = Literal[
  "eager",
  "lazy",
]
ImgReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
InputAcceptL = Literal[
  "audio/*",
  "video/*",
  "image/*",
]
InputAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
InputFormenctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
InputFormmethodL = Literal[
  "get",
  "post",
]
InputFormtargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
InputTypeL = Literal[
  "button",
  "checkbox",
  "color",
  "date",
  "datetime",
  "datetime-local",
  "email",
  "file",
  "hidden",
  "image",
  "month",
  "number",
  "password",
  "radio",
  "range",
  "reset",
  "search",
  "submit",
  "tel",
  "text",
  "time",
  "url",
  "week",
]
InputmodeL = Literal[
  "email",
  "full-width-latin",
  "kana",
  "kana-name",
  "katakana",
  "latin",
  "latin-name",
  "latin-prose",
  "numeric",
  "tel",
  "url",
  "verbatim",
]
LinkCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
LinkReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
LinkRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "stylesheet",
  "tag",
]
MetaHttp_equivL = Literal[
  "content-security-policy",
  "content-type",
  "default-style",
  "refresh",
]
MetaNameL = Literal[
  "application-name",
  "author",
  "description",
  "generator",
  "keywords",
  "viewport",
]
OlTypeL = Literal[
  "1",
  "A",
  "I",
  "a",
  "i",
]
RoleL = Literal[
  "alert",
  "alertdialog",
  "application",
  "article",
  "banner",
  "button",
  "cell",
  "checkbox",
  "columnheader",
  "combobox",
  "complementary",
  "contentinfo",
  "definition",
  "dialog",
  "directory",
  "doc-abstract",
  "doc-acknowledgments",
  "doc-afterword",
  "doc-appendix",
  "doc-backlink",
  "doc-biblioentry",
  "doc-bibliography",
  "doc-biblioref",
  "doc-chapter",
  "doc-colophon",
  "doc-conclusion",
  "doc-cover",
  "doc-credit",
  "doc-credits",
  "doc-dedication",
  "doc-endnote",
  "doc-endnotes",
  "doc-epigraph",
  "doc-epilogue",
  "doc-errata",
  "doc-example",
  "doc-footnote",
  "doc-foreword",
  "doc-glossary",
  "doc-glossref",
  "doc-index",
  "doc-introduction",
  "doc-noteref",
  "doc-notice",
  "doc-pagebreak",
  "doc-pagelist",
  "doc-part",
  "doc-preface",
  "doc-prologue",
  "doc-pullquote",
  "doc-qna",
  "doc-subtitle",
  "doc-tip",
  "doc-toc",
  "document",
  "feed",
  "figure",
  "form",
  "grid",
  "gridcell",
  "group",
  "heading",
  "img",
  "link",
  "list",
  "listbox",
  "listitem",
  "log",
  "main",
  "marquee",
  "math",
  "menu",
  "menubar",
  "menuitem",
  "menuitemcheckbox",
  "menuitemradio",
  "navigation",
  "none",
  "note",
  "option",
  "presentation",
  "progressbar",
  "radio",
  "radiogroup",
  "region",
  "region",
  "row",
  "rowgroup",
  "rowheader",
  "scrollbar",
  "search",
  "searchbox",
  "separator",
  "slider",
  "spinbutton",
  "status",
  "switch",
  "tab",
  "table",
  "tablist",
  "tabpanel",
  "term",
  "text",
  "textbox",
  "timer",
  "toolbar",
  "tooltip",
  "tree",
  "treegrid",
  "treeitem",
]
ScriptCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
ScriptReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
SelectAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
SpellcheckL = Literal[
  "false",
  "true",
]
TextareaAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
TextareaSpellcheckL = Literal[
  "default",
  "false",
  "true",
]
TextareaWrapL = Literal[
  "hard",
  "soft",
]
ThScopeL = Literal[
  "col",
  "colgroup",
  "row",
  "rowgroup",
]
TrackKindL = Literal[
  "captions",
  "chapters",
  "descriptions",
  "metadata",
  "subtitles",
]
TranslateL = Literal[
  "no",
  "yes",
]
VideoCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
VideoPreloadL = Literal[
  "auto",
  "metadata",
  "none",
]
#endregion

from typing import TypedDict

class GlobalAttrs(TypedDict, total=False):
  aria: dict[str, str]
  data: dict[str, str]
  user: dict[str, str]
  h_accesskey: str
  h_autocapitalize: str
  h_autofocus: bool
  h_class: str
  h_contenteditable: str
  h_dir: DirL
  h_draggable: DraggableL
  h_enterkeyhint: str
  h_hidden: bool
  h_id: str
  h_inert: bool
  h_inputmode: InputmodeL
  h_is: str
  h_itemid: str
  h_itemprop: str
  h_itemref: str
  h_itemscope: bool
  h_itemtype: str
  h_lang: str
  h_nonce: str
  h_part: str
  h_popover: str
  h_role: RoleL
  h_slot: str
  h_spellcheck: SpellcheckL
  h_style: str
  h_tabindex: str
  h_title: str
  h_translate: TranslateL
  h_virtualkeyboardpolicy: str

  h__: str
  h_script: str
  hx_boost: str
  hx_confirm: str
  hx_delete: str
  hx_disable: str
  hx_disabled_elt: str
  hx_disinherit: str
  hx_encoding: str
  hx_ext: str
  hx_get: str
  hx_headers: str
  hx_history_elt: str
  hx_history: str
  hx_include: str
  hx_indicator: str
  hx_inherit: str
  hx_on: str
  hx_params: str
  hx_patch: str
  hx_post: str
  hx_preserve: str
  hx_prompt: str
  hx_push_url: str
  hx_put: str
  hx_replace_url: str
  hx_request: str
  hx_select_oob: str
  hx_select: str
  hx_swap_oob: str
  hx_swap: str
  hx_sync: str
  hx_target: str
  hx_trigger: str
  hx_validate: str
  hx_vals: str
  hx_vars: str

class AAttrs(GlobalAttrs, total=False):
  h_download: str
  h_href: str
  h_hreflang: str
  h_ping: str
  h_referrerpolicy: AReferrerpolicyL
  h_rel: ARelL
  h_target: ATargetL
  h_type: str

class AreaAttrs(GlobalAttrs, total=False):
  h_alt: str
  h_coords: str
  h_download: str
  h_href: str
  h_ping: str
  h_referrerpolicy: AreaReferrerpolicyL
  h_rel: AreaRelL
  h_shape: AreaShapeL
  h_target: AreaTargetL

class AudioAttrs(GlobalAttrs, total=False):
  h_autoplay: bool
  h_controls: bool
  h_crossorigin: AudioCrossoriginL
  h_loop: bool
  h_muted: bool
  h_preload: AudioPreloadL
  h_src: str

class BaseAttrs(GlobalAttrs, total=False):
  h_href: str
  h_target: BaseTargetL

class BlockquoteAttrs(GlobalAttrs, total=False):
  h_cite: str

class BodyAttrs(GlobalAttrs, total=False):
  h_onafterprint: str
  h_onbeforeprint: str
  h_onbeforeunload: str
  h_onblur: str
  h_onerror: str
  h_onfocus: str
  h_onhashchange: str
  h_onlanguagechange: str
  h_onload: str
  h_onmessage: str
  h_onoffline: str
  h_ononline: str
  h_onpopstate: str
  h_onredo: str
  h_onresize: str
  h_onstorage: str
  h_onundo: str
  h_onunload: str

class ButtonAttrs(GlobalAttrs, total=False):
  h_autofocus: bool
  h_disabled: bool
  h_form: str
  h_formaction: str
  h_formenctype: ButtonFormenctypeL
  h_formmethod: ButtonFormmethodL
  h_formnovalidate: bool
  h_formtarget: ButtonFormtargetL
  h_name: str
  h_type: ButtonTypeL
  h_value: str

class CanvasAttrs(GlobalAttrs, total=False):
  h_height: str
  h_width: str

class ColAttrs(GlobalAttrs, total=False):
  h_span: str

class ColgroupAttrs(GlobalAttrs, total=False):
  h_span: str

class DataAttrs(GlobalAttrs, total=False):
  h_value: str

class DelAttrs(GlobalAttrs, total=False):
  h_cite: str
  h_datetime: str

class DetailsAttrs(GlobalAttrs, total=False):
  h_open: bool

class DialogAttrs(GlobalAttrs, total=False):
  h_open: bool

class EmbedAttrs(GlobalAttrs, total=False):
  h_height: str
  h_src: str
  h_type: str
  h_width: str

class FieldsetAttrs(GlobalAttrs, total=False):
  h_disabled: bool
  h_form: str
  h_name: str

class FormAttrs(GlobalAttrs, total=False):
  h_accept_charset: str
  h_action: str
  h_autocomplete: FormAutocompleteL
  h_enctype: FormEnctypeL
  h_method: FormMethodL
  h_name: str
  h_novalidate: bool
  h_rel: FormRelL
  h_target: FormTargetL

class HtmlAttrs(GlobalAttrs, total=False):
  h_xmlns: HtmlXmlnsL

class IframeAttrs(GlobalAttrs, total=False):
  h_allow: str
  h_allowfullscreen: IframeAllowfullscreenL
  h_height: str
  h_loading: IframeLoadingL
  h_name: str
  h_referrerpolicy: IframeReferrerpolicyL
  h_sandbox: IframeSandboxL
  h_src: str
  h_srcdoc: str
  h_width: str

class ImgAttrs(GlobalAttrs, total=False):
  h_alt: str
  h_crossorigin: ImgCrossoriginL
  h_decoding: ImgDecodingL
  h_fetchpriority: ImgFetchpriorityL
  h_height: str
  h_ismap: bool
  h_loading: ImgLoadingL
  h_referrerpolicy: ImgReferrerpolicyL
  h_sizes: str
  h_src: str
  h_srcset: str
  h_usemap: str
  h_width: str

class InputAttrs(GlobalAttrs, total=False):
  h_accept: InputAcceptL
  h_alt: str
  h_autocomplete: InputAutocompleteL
  h_autofocus: bool
  h_capture: str
  h_checked: bool
  h_dirname: str
  h_disabled: bool
  h_form: str
  h_formaction: str
  h_formenctype: InputFormenctypeL
  h_formmethod: InputFormmethodL
  h_formnovalidate: bool
  h_formtarget: InputFormtargetL
  h_height: str
  h_list: str
  h_max: str
  h_maxlength: str
  h_min: str
  h_minlength: str
  h_multiple: bool
  h_name: str
  h_pattern: str
  h_placeholder: str
  h_readonly: bool
  h_required: bool
  h_size: str
  h_src: str
  h_step: str
  h_type: InputTypeL
  h_value: str
  h_width: str

class InsAttrs(GlobalAttrs, total=False):
  h_cite: str
  h_datetime: str

class LabelAttrs(GlobalAttrs, total=False):
  h_for: str

class LiAttrs(GlobalAttrs, total=False):
  h_value: str

class LinkAttrs(GlobalAttrs, total=False):
  h_as: str
  h_crossorigin: LinkCrossoriginL
  h_fetchpriority: str
  h_href: str
  h_hreflang: str
  h_imagesizes: str
  h_imagesrcset: str
  h_integrity: str
  h_media: str
  h_referrerpolicy: LinkReferrerpolicyL
  h_rel: LinkRelL
  h_sizes: str
  h_type: str

class MapAttrs(GlobalAttrs, total=False):
  h_name: str

class MetaAttrs(GlobalAttrs, total=False):
  h_charset: str
  h_content: str
  h_http_equiv: MetaHttp_equivL
  h_name: MetaNameL

class MeterAttrs(GlobalAttrs, total=False):
  h_form: str
  h_high: str
  h_low: str
  h_max: str
  h_min: str
  h_optimum: str
  h_value: str

class ObjectAttrs(GlobalAttrs, total=False):
  h_data: str
  h_form: str
  h_height: str
  h_name: str
  h_type: str
  h_width: str

class OlAttrs(GlobalAttrs, total=False):
  h_reversed: bool
  h_start: str
  h_type: OlTypeL

class OptgroupAttrs(GlobalAttrs, total=False):
  h_disabled: bool
  h_label: str

class OptionAttrs(GlobalAttrs, total=False):
  h_disabled: bool
  h_label: str
  h_selected: bool
  h_value: str | int | float

class OutputAttrs(GlobalAttrs, total=False):
  h_for: str
  h_form: str
  h_name: str

class ProgressAttrs(GlobalAttrs, total=False):
  h_max: str
  h_value: str

class QAttrs(GlobalAttrs, total=False):
  h_cite: str

class ScriptAttrs(GlobalAttrs, total=False):
  h_async: bool
  h_crossorigin: ScriptCrossoriginL
  h_defer: bool
  h_fetchpriority: str
  h_integrity: str
  h_nomodule: bool
  h_nonce: str
  h_referrerpolicy: ScriptReferrerpolicyL
  h_src: str
  h_type: str

class SelectAttrs(GlobalAttrs, total=False):
  h_autocomplete: SelectAutocompleteL
  h_autofocus: bool
  h_disabled: bool
  h_form: str
  h_multiple: bool
  h_name: str
  h_required: bool
  h_size: str

class SlotAttrs(GlobalAttrs, total=False):
  h_name: str

class SourceAttrs(GlobalAttrs, total=False):
  h_height: str
  h_media: str
  h_sizes: str
  h_src: str
  h_srcset: str
  h_type: str
  h_width: str

class StyleAttrs(GlobalAttrs, total=False):
  h_blocking: str
  h_media: str
  h_nonce: str
  h_title: str

class TdAttrs(GlobalAttrs, total=False):
  h_colspan: str
  h_headers: str
  h_rowspan: str

class TextareaAttrs(GlobalAttrs, total=False):
  h_autocomplete: TextareaAutocompleteL
  h_autofocus: bool
  h_cols: str
  h_dirname: str
  h_disabled: bool
  h_form: str
  h_maxlength: str
  h_minlength: str
  h_name: str
  h_placeholder: str
  h_readonly: bool
  h_required: bool
  h_rows: str
  h_spellcheck: TextareaSpellcheckL
  h_wrap: TextareaWrapL

class ThAttrs(GlobalAttrs, total=False):
  h_abbr: str
  h_colspan: str
  h_headers: str
  h_rowspan: str
  h_scope: ThScopeL

class TimeAttrs(GlobalAttrs, total=False):
  h_datetime: str

class TrackAttrs(GlobalAttrs, total=False):
  h_default: bool
  h_kind: TrackKindL
  h_label: str
  h_src: str
  h_srclang: str

class VideoAttrs(GlobalAttrs, total=False):
  h_autoplay: bool
  h_controls: bool
  h_crossorigin: VideoCrossoriginL
  h_disableremoteplayback: bool
  h_loop: bool
  h_muted: bool
  h_playsinline: bool
  h_poster: str
  h_preload: VideoPreloadL
  h_src: str
  h_width: str
