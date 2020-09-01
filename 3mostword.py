import string
import re

def top_3_words(text):
	text = text.lower()

	#s = string.punctuation
	s = '!()-[]{};:<>."/?@#$%^&*_~,'

	new_text = set((' '.join(word.strip(s) for word in re.split(r'[^a-zA-Z\']+',text))).split())

	return new_text


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  //wont won't won't "))
print(top_3_words("  , e   .. "))
print(top_3_words("  __'ba?::'ba "))
print(top_3_words("  'tts  "))
print(top_3_words("  '''  "))
print(top_3_words("hxaid-/hxaid;;,;!ttiznkufgb_?.fwykf-_. pwcbn_,.xni.-!yhwpychz.pwcbn,.,:pwcbn-ueh'_?yhwpychz;!.ttiznkufgb??-,qhlebahxy: pwcbn,.,-.vqlmnphmrz:.!pwcbn:ltsjztgqfz!,;_:ywy-._ppmnmuw;/-njgnzcpaa;:ttiznkufgb._ttiznkufgb,__/ueh';:pwcbn_ueh'_;?,xni/!sqa.-ywy .;- ueh'-,-,:ltsjztgqfz/yhwpychz/!-,;ltsjztgqfz;-ttiznkufgb  .njgnzcpaa?:ywy..;pwcbn:! /_ltsjztgqfz?/_..hxaid?/!,:fwykf, ,ueh';njgnzcpaa:;_ltsjztgqfz,!;hxaid/!hxaid?!_,?ltsjztgqfz-,/__hxaid!-fwykf.._vqlmnphmrz_: .ueh'!.-pwcbn;_-hxaid_:-,qhlebahxy_//_!yhwpychz !; hxaid ; vqlmnphmrz xni.-ltsjztgqfz_:,/;xni/ppmnmuw//_:/sqa_-;yhwpychz/_ ?ueh'!njgnzcpaa-?;,ltsjztgqfz:.!,aueloblbv: njgnzcpaa?.xni?/-?:sqa /hxaid!fwykf-,:.xni..hxaid,:;-sqa!--:-ywy? vqlmnphmrz::xni, ueh'/ .sqa // /pwcbn,!_ppmnmuw??-sqa !_-ttiznkufgb_/_,yhwpychz;!:, ppmnmuw__.yhwpychz:pwcbn/ !ltsjztgqfz!/ltsjztgqfz/pwcbn/pwcbn?-ttiznkufgb/_,;;fwykf/!ueh' ltsjztgqfz., pwcbn sqa!hxaid!ttiznkufgb yhwpychz?:yhwpychz ?pwcbn:/__;yhwpychz:yhwpychz?;_sqa!-?sqa?!!!-xni!ppmnmuw-ttiznkufgb/ -ywy_/njgnzcpaa ; ,,ttiznkufgb _. .njgnzcpaa:- -yhwpychz!/-pwcbn/-/;,yhwpychz/!/-qhlebahxy/-,_sqa;/hxaid;;aueloblbv__;_/vqlmnphmrz, ltsjztgqfz.,?yhwpychz?!-,hxaid;pwcbn_,qhlebahxy/pwcbn: _ttiznkufgb ?,,;vqlmnphmrz;;;.-qhlebahxy::!?sqa,.hxaid!/! pwcbn-ueh'.?_:.aueloblbv/ttiznkufgb?ltsjztgqfz_/pwcbn_ltsjztgqfz;!hxaid:.!sqa./!ueh',;/,pwcbn-_?,-hxaid/!!, ppmnmuw./_?njgnzcpaa_.-?yhwpychz: -ttiznkufgb:-qhlebahxy:_/pwcbn,/:!.ltsjztgqfz/_yhwpychz- ?yhwpychz.pwcbn__hxaid?_ttiznkufgb!?!_pwcbn?!pwcbn:?.ttiznkufgb_--njgnzcpaa-sqa:ttiznkufgb--:yhwpychz/_ :ttiznkufgb?,_pwcbn! ,/.sqa;!/ywy ,-sqa//.!/sqa/:pwcbn?.ueh'-vqlmnphmrz;,,qhlebahxy ?/_hxaid:njgnzcpaa _yhwpychz_;!_sqa_?;;!fwykf;!..yhwpychz; ?qhlebahxy_!_;njgnzcpaa-?_,xni.!__/sqa/: /:ttiznkufgb_ttiznkufgb?! ;.hxaid_yhwpychz_./qhlebahxy,,;,ltsjztgqfz: -ueh', ttiznkufgb pwcbn,?hxaid,!qhlebahxy!,._ueh'?!:fwykf, /vqlmnphmrz-..!vqlmnphmrz:;?-ueh'-../ qhlebahxy;fwykf-,?:njgnzcpaa;ttiznkufgb?njgnzcpaa,?ttiznkufgb:_?vqlmnphmrz/ttiznkufgb..,!sqa?..yhwpychz/;_ueh'..qhlebahxy?sqa/?  ttiznkufgb:_-qhlebahxy :-.pwcbn_; ;ueh'_,;.yhwpychz::-ttiznkufgb:ltsjztgqfz!/ fwykf_pwcbn, ;:ttiznkufgb-ueh',!ttiznkufgb___xni/!njgnzcpaa!;!-?ltsjztgqfz--_-;sqa!:-,!ltsjztgqfz.xni;fwykf;/:-_"))