<map version="freeplane 1.6.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Python" FOLDED="false" ID="ID_845831299" CREATED="1505379763442" MODIFIED="1505379772034" STYLE="oval"><hook NAME="MapStyle">
    <conditional_styles>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.connection" LAST="false">
            <node_periodic_level_condition PERIOD="2" REMAINDER="1"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.topic" LAST="false">
            <node_level_condition VALUE="2" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.subtopic" LAST="false">
            <node_level_condition VALUE="4" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
        <conditional_style ACTIVE="true" LOCALIZED_STYLE_REF="styles.subsubtopic" LAST="false">
            <node_level_condition VALUE="6" MATCH_CASE="false" MATCH_APPROXIMATELY="false" COMPARATION_RESULT="0" SUCCEED="true"/>
        </conditional_style>
    </conditional_styles>
    <properties fit_to_viewport="false" edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="Arial" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.connection" COLOR="#606060" STYLE="fork">
<font NAME="Arial" SIZE="8" BOLD="false"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="Tutorials" POSITION="right" ID="ID_396810689" CREATED="1505379773237" MODIFIED="1505379780279">
<node TEXT="https://learnxinyminutes.com/docs/python/" ID="ID_1395890656" CREATED="1505379790702" MODIFIED="1505379953436" LINK="https://learnxinyminutes.com/docs/python/"/>
<node TEXT="https://automatetheboringstuff.com/" ID="ID_968951289" CREATED="1505455412139" MODIFIED="1505455440488" LINK="https://automatetheboringstuff.com/">
<node TEXT="Automate the Boring Stuff with Python" ID="ID_90271225" CREATED="1505455466830" MODIFIED="1505455473074"/>
<node TEXT="Al Sweigart" ID="ID_48730714" CREATED="1505455526753" MODIFIED="1505455534739"/>
</node>
<node TEXT="Hello world! Computer Programming for Kids and Other Beginners" ID="ID_1544036012" CREATED="1505455753325" MODIFIED="1505456197513" LINK="http://home.ustc.edu.cn/~ustcsh/py2016/data/Warren%20Sande,%20Carter%20Sande-Hello%20World!_%20Computer%20Programming%20for%20Kids%20and%20Other%20Beginners-Manning%20Publications.pdf">
<node TEXT="Warren Sande" ID="ID_1951519723" CREATED="1505455791007" MODIFIED="1505456159641"/>
<node TEXT="Carter Sande" ID="ID_1100679243" CREATED="1505456131480" MODIFIED="1505456137833"/>
</node>
</node>
<node TEXT="String" POSITION="left" ID="ID_1951269290" CREATED="1505379884074" MODIFIED="1505379886308"/>
<node TEXT="global function" POSITION="right" ID="ID_273043413" CREATED="1505379889186" MODIFIED="1505379893148">
<node TEXT="len()" ID="ID_609202827" CREATED="1505379893547" MODIFIED="1505379895949"/>
<node TEXT="input()" ID="ID_1144735550" CREATED="1505526561754" MODIFIED="1505526564869"/>
<node TEXT="type()" ID="ID_454050372" CREATED="1505552190949" MODIFIED="1505552192916"/>
<node TEXT="raw_input()" ID="ID_1791361975" CREATED="1505553003648" MODIFIED="1505553007395"/>
<node TEXT="" ID="ID_1954736708" CREATED="1505553016317" MODIFIED="1505553016317"/>
</node>
<node TEXT="GUI" POSITION="left" ID="ID_1481921201" CREATED="1505520582727" MODIFIED="1505520584551">
<node TEXT="PyQt" ID="ID_69416610" CREATED="1505520585397" MODIFIED="1505520588742"/>
<node TEXT="EasyGUI" ID="ID_1842030416" CREATED="1505558826593" MODIFIED="1505558833303">
<node TEXT="easygui" ID="ID_42527795" CREATED="1505571994452" MODIFIED="1505571997247">
<node TEXT="msgbox(title)" ID="ID_532364304" CREATED="1505572010575" MODIFIED="1505572017890"/>
<node TEXT="buttonbox(title, choices=[])" ID="ID_232018782" CREATED="1505658271195" MODIFIED="1505658299528"/>
<node TEXT="choicebox(title, choices=[])" ID="ID_766726156" CREATED="1505658582167" MODIFIED="1505658611055"/>
<node TEXT="enterbox(title)" ID="ID_134710041" CREATED="1505693334138" MODIFIED="1505693338657">
<node TEXT="just like raw_input()" ID="ID_1756599251" CREATED="1505695000476" MODIFIED="1505695008889"/>
</node>
<node TEXT="integerbox(title)" ID="ID_143383213" CREATED="1505695218662" MODIFIED="1505695223923">
<node TEXT="only accept integers" ID="ID_375539377" CREATED="1505695225025" MODIFIED="1505695232676"/>
</node>
</node>
</node>
</node>
<node TEXT="random" POSITION="right" ID="ID_978555833" CREATED="1505526330117" MODIFIED="1505526333473">
<node TEXT="randint(a, b)" ID="ID_1002238845" CREATED="1505526349749" MODIFIED="1505526356251"/>
</node>
<node TEXT="Types of Datas" POSITION="left" ID="ID_572810602" CREATED="1505549741133" MODIFIED="1505549754739"/>
<node TEXT="urllib2" POSITION="right" ID="ID_1801942785" CREATED="1505555336669" MODIFIED="1505555469899">
<icon BUILTIN="full-2"/>
<node TEXT="urlopen(url)" ID="ID_1077960610" CREATED="1505555353613" MODIFIED="1505555358851">
<node TEXT="return a file-like object" ID="ID_1052481852" CREATED="1505555785401" MODIFIED="1505555790413">
<node TEXT="read()" ID="ID_1717006277" CREATED="1505555797464" MODIFIED="1505555800117"/>
</node>
</node>
</node>
<node TEXT="urllib" POSITION="right" ID="ID_1859594214" CREATED="1505555751464" MODIFIED="1505555756075">
<icon BUILTIN="full-3"/>
<node TEXT="request" ID="ID_1613444165" CREATED="1505555772699" MODIFIED="1505555775233"/>
<node TEXT="error" ID="ID_671271337" CREATED="1505555775558" MODIFIED="1505555776977"/>
</node>
</node>
</map>
