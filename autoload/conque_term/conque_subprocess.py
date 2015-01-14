



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = null;
 
 
 var CS_env = {"assetHostPath": "https://ssl.gstatic.com/codesite/ph", "token": null, "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/18133036155640238800", "domainName": null, "loggedInUserEmail": null, "relativeBaseUrl": "", "profileUrl": null, "projectName": "conque", "projectHomeUrl": "/p/conque"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 _gaq.push(
 ['projectTracker._setAccount', 'UA-23164955-1'],
 ['projectTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>conque_subprocess.py - 
 conque -
 
 
 Run interactive commands inside a Vim buffer - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/18133036155640238800/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/18133036155640238800/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/18133036155640238800/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/18133036155640238800/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 <a href="#" id="projects-dropdown" onclick="return false;"><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fconque%2Fsource%2Fbrowse%2Fbranches%2Fpython3%2Fautoload%2Fconque_subprocess.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fconque%2Fsource%2Fbrowse%2Fbranches%2Fpython3%2Fautoload%2Fconque_subprocess.py" onclick="_CS_click('/gb/ph/signin');"><u>Sign in</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/conque">
 <a href="/p/conque/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/conque/"><span itemprop="name">conque</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/conque/"><span itemprop="description">Run interactive commands inside a Vim buffer</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/conque/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 <a href="/p/conque/downloads/list" class="tab ">Downloads</a>
 
 
 
 
 
 <a href="/p/conque/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/conque/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/conque/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/conque/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/conque/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/conque/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/conque/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/conque/source/browse/branches/">branches</a><span class="sp">/&nbsp;</span><a href="/p/conque/source/browse/branches/python3/">python3</a><span class="sp">/&nbsp;</span><a href="/p/conque/source/browse/branches/python3/autoload/">autoload</a><span class="sp">/&nbsp;</span>conque_subprocess.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/conque/source/browse/branches/python3/autoload/conque_subprocess.py?r=234" title="Previous">&lsaquo;r234</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>r496</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn496_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn496_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn496_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn496_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn496_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn496_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn496_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn496_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn496_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn496_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn496_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn496_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn496_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn496_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn496_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn496_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn496_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn496_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn496_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn496_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn496_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn496_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn496_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn496_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn496_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn496_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn496_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn496_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn496_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn496_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn496_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn496_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn496_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn496_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn496_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn496_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn496_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn496_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn496_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn496_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn496_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn496_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn496_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn496_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn496_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn496_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn496_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn496_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn496_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn496_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn496_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn496_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn496_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn496_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn496_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn496_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn496_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn496_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn496_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn496_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn496_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn496_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn496_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn496_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn496_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn496_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn496_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn496_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn496_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn496_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn496_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn496_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn496_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn496_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn496_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn496_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn496_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn496_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn496_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn496_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn496_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn496_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn496_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn496_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn496_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn496_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn496_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn496_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn496_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn496_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn496_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn496_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn496_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn496_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn496_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn496_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn496_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn496_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn496_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn496_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn496_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn496_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn496_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn496_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn496_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn496_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn496_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn496_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn496_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn496_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn496_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn496_112"

><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn496_113"

><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn496_114"

><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn496_115"

><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn496_116"

><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn496_117"

><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn496_118"

><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn496_119"

><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn496_120"

><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn496_121"

><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn496_122"

><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn496_123"

><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn496_124"

><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn496_125"

><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn496_126"

><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn496_127"

><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn496_128"

><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn496_129"

><td id="129"><a href="#129">129</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn496_1

><td class="source"><br></td></tr
><tr
id=sl_svn496_2

><td class="source">import os, signal, pty, tty, select, fcntl, termios, struct<br></td></tr
><tr
id=sl_svn496_3

><td class="source"><br></td></tr
><tr
id=sl_svn496_4

><td class="source">###################################################################################################<br></td></tr
><tr
id=sl_svn496_5

><td class="source">class ConqueSubprocess:<br></td></tr
><tr
id=sl_svn496_6

><td class="source"><br></td></tr
><tr
id=sl_svn496_7

><td class="source">    # process id<br></td></tr
><tr
id=sl_svn496_8

><td class="source">    pid = 0<br></td></tr
><tr
id=sl_svn496_9

><td class="source">    <br></td></tr
><tr
id=sl_svn496_10

><td class="source">    # stdout+stderr file descriptor<br></td></tr
><tr
id=sl_svn496_11

><td class="source">    fd = None<br></td></tr
><tr
id=sl_svn496_12

><td class="source"><br></td></tr
><tr
id=sl_svn496_13

><td class="source">    # constructor<br></td></tr
><tr
id=sl_svn496_14

><td class="source">    def __init__(self): # {{{<br></td></tr
><tr
id=sl_svn496_15

><td class="source">        self.pid = 0<br></td></tr
><tr
id=sl_svn496_16

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_17

><td class="source"><br></td></tr
><tr
id=sl_svn496_18

><td class="source">    # create the pty or whatever (whatever == windows)<br></td></tr
><tr
id=sl_svn496_19

><td class="source">    def open(self, command, env = {}): # {{{<br></td></tr
><tr
id=sl_svn496_20

><td class="source">        command_arr  = command.split()<br></td></tr
><tr
id=sl_svn496_21

><td class="source">        executable   = command_arr[0]<br></td></tr
><tr
id=sl_svn496_22

><td class="source">        args         = command_arr<br></td></tr
><tr
id=sl_svn496_23

><td class="source"><br></td></tr
><tr
id=sl_svn496_24

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_25

><td class="source">            self.pid, self.fd = pty.fork()<br></td></tr
><tr
id=sl_svn496_26

><td class="source">            logging.debug(self.pid)<br></td></tr
><tr
id=sl_svn496_27

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_28

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_29

><td class="source">            logging.debug(&quot;pty.fork() failed. Did you mean pty.spork() ???&quot;)<br></td></tr
><tr
id=sl_svn496_30

><td class="source"><br></td></tr
><tr
id=sl_svn496_31

><td class="source">        # child proc, replace with command after altering terminal attributes<br></td></tr
><tr
id=sl_svn496_32

><td class="source">        if self.pid == 0:<br></td></tr
><tr
id=sl_svn496_33

><td class="source"><br></td></tr
><tr
id=sl_svn496_34

><td class="source">            # set requested environment variables<br></td></tr
><tr
id=sl_svn496_35

><td class="source">            for k in env.keys():<br></td></tr
><tr
id=sl_svn496_36

><td class="source">                os.environ[k] = env[k]<br></td></tr
><tr
id=sl_svn496_37

><td class="source"><br></td></tr
><tr
id=sl_svn496_38

><td class="source">            # set some attributes<br></td></tr
><tr
id=sl_svn496_39

><td class="source">            try:<br></td></tr
><tr
id=sl_svn496_40

><td class="source">                attrs = tty.tcgetattr(1)<br></td></tr
><tr
id=sl_svn496_41

><td class="source">                attrs[0] = attrs[0] ^ tty.IGNBRK<br></td></tr
><tr
id=sl_svn496_42

><td class="source">                attrs[0] = attrs[0] | tty.BRKINT | tty.IXANY | tty.IMAXBEL<br></td></tr
><tr
id=sl_svn496_43

><td class="source">                attrs[2] = attrs[2] | tty.HUPCL<br></td></tr
><tr
id=sl_svn496_44

><td class="source">                attrs[3] = attrs[3] | tty.ICANON | tty.ECHO | tty.ISIG | tty.ECHOKE<br></td></tr
><tr
id=sl_svn496_45

><td class="source">                attrs[6][tty.VMIN]  = 1<br></td></tr
><tr
id=sl_svn496_46

><td class="source">                attrs[6][tty.VTIME] = 0<br></td></tr
><tr
id=sl_svn496_47

><td class="source">                tty.tcsetattr(1, tty.TCSANOW, attrs)<br></td></tr
><tr
id=sl_svn496_48

><td class="source">            except:<br></td></tr
><tr
id=sl_svn496_49

><td class="source">                pass<br></td></tr
><tr
id=sl_svn496_50

><td class="source"><br></td></tr
><tr
id=sl_svn496_51

><td class="source">            os.execvp(executable, args)<br></td></tr
><tr
id=sl_svn496_52

><td class="source"><br></td></tr
><tr
id=sl_svn496_53

><td class="source">        # else master, do nothing<br></td></tr
><tr
id=sl_svn496_54

><td class="source">        else:<br></td></tr
><tr
id=sl_svn496_55

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_56

><td class="source"><br></td></tr
><tr
id=sl_svn496_57

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_58

><td class="source"><br></td></tr
><tr
id=sl_svn496_59

><td class="source">    # read from pty<br></td></tr
><tr
id=sl_svn496_60

><td class="source">    # XXX - select.poll() doesn&#39;t work in OS X!!!!!!!<br></td></tr
><tr
id=sl_svn496_61

><td class="source">    def read(self, timeout = 1): # {{{<br></td></tr
><tr
id=sl_svn496_62

><td class="source"><br></td></tr
><tr
id=sl_svn496_63

><td class="source">        output = &#39;&#39;<br></td></tr
><tr
id=sl_svn496_64

><td class="source">        read_timeout = float(timeout) / 1000<br></td></tr
><tr
id=sl_svn496_65

><td class="source"><br></td></tr
><tr
id=sl_svn496_66

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_67

><td class="source">            # what, no do/while?<br></td></tr
><tr
id=sl_svn496_68

><td class="source">            while 1:<br></td></tr
><tr
id=sl_svn496_69

><td class="source">                s_read, s_write, s_error = select.select( [ self.fd ], [], [], read_timeout)<br></td></tr
><tr
id=sl_svn496_70

><td class="source"><br></td></tr
><tr
id=sl_svn496_71

><td class="source">                lines = &#39;&#39;<br></td></tr
><tr
id=sl_svn496_72

><td class="source">                for s_fd in s_read:<br></td></tr
><tr
id=sl_svn496_73

><td class="source">                    try:<br></td></tr
><tr
id=sl_svn496_74

><td class="source">                        lines = os.read( self.fd, 32 )<br></td></tr
><tr
id=sl_svn496_75

><td class="source">                    except:<br></td></tr
><tr
id=sl_svn496_76

><td class="source">                        pass<br></td></tr
><tr
id=sl_svn496_77

><td class="source">                    output = output + lines.decode(&#39;utf-8&#39;)<br></td></tr
><tr
id=sl_svn496_78

><td class="source"><br></td></tr
><tr
id=sl_svn496_79

><td class="source">                if lines == &#39;&#39;:<br></td></tr
><tr
id=sl_svn496_80

><td class="source">                    break<br></td></tr
><tr
id=sl_svn496_81

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_82

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_83

><td class="source"><br></td></tr
><tr
id=sl_svn496_84

><td class="source">        return output<br></td></tr
><tr
id=sl_svn496_85

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_86

><td class="source"><br></td></tr
><tr
id=sl_svn496_87

><td class="source">    # I guess this one&#39;s not bad<br></td></tr
><tr
id=sl_svn496_88

><td class="source">    def write(self, input): # {{{<br></td></tr
><tr
id=sl_svn496_89

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_90

><td class="source">            os.write(self.fd, bytes(input, &#39;utf-8&#39;))<br></td></tr
><tr
id=sl_svn496_91

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_92

><td class="source">            logging.debug(&#39;write fail&#39;)<br></td></tr
><tr
id=sl_svn496_93

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_94

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_95

><td class="source"><br></td></tr
><tr
id=sl_svn496_96

><td class="source">    # signal process<br></td></tr
><tr
id=sl_svn496_97

><td class="source">    def signal(self, signum): # {{{<br></td></tr
><tr
id=sl_svn496_98

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_99

><td class="source">            os.kill(self.pid, signum)<br></td></tr
><tr
id=sl_svn496_100

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_101

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_102

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_103

><td class="source"><br></td></tr
><tr
id=sl_svn496_104

><td class="source">    # get process status<br></td></tr
><tr
id=sl_svn496_105

><td class="source">    def get_status(self): #{{{<br></td></tr
><tr
id=sl_svn496_106

><td class="source"><br></td></tr
><tr
id=sl_svn496_107

><td class="source">        p_status = True<br></td></tr
><tr
id=sl_svn496_108

><td class="source"><br></td></tr
><tr
id=sl_svn496_109

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_110

><td class="source">            if os.waitpid( self.pid, os.WNOHANG )[0]:<br></td></tr
><tr
id=sl_svn496_111

><td class="source">                p_status = False<br></td></tr
><tr
id=sl_svn496_112

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_113

><td class="source">            p_status = False<br></td></tr
><tr
id=sl_svn496_114

><td class="source"><br></td></tr
><tr
id=sl_svn496_115

><td class="source">        return p_status<br></td></tr
><tr
id=sl_svn496_116

><td class="source"><br></td></tr
><tr
id=sl_svn496_117

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_118

><td class="source"><br></td></tr
><tr
id=sl_svn496_119

><td class="source">    # update window size in kernel, then send SIGWINCH to fg process<br></td></tr
><tr
id=sl_svn496_120

><td class="source">    def window_resize(self, lines, columns): # {{{<br></td></tr
><tr
id=sl_svn496_121

><td class="source">        try:<br></td></tr
><tr
id=sl_svn496_122

><td class="source">            fcntl.ioctl(self.fd, termios.TIOCSWINSZ, struct.pack(&quot;HHHH&quot;, lines, columns, 0, 0))<br></td></tr
><tr
id=sl_svn496_123

><td class="source">            os.kill(self.pid, signal.SIGWINCH)<br></td></tr
><tr
id=sl_svn496_124

><td class="source">        except:<br></td></tr
><tr
id=sl_svn496_125

><td class="source">            pass<br></td></tr
><tr
id=sl_svn496_126

><td class="source"><br></td></tr
><tr
id=sl_svn496_127

><td class="source">        # }}}<br></td></tr
><tr
id=sl_svn496_128

><td class="source"><br></td></tr
><tr
id=sl_svn496_129

><td class="source"><br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn496_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn496_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/conque/source/detail?spec=svn496&amp;r=236">r236</a>
 by nicoraffo
 on Jul 22, 2010
 &nbsp; <a href="/p/conque/source/diff?spec=svn496&r=236&amp;format=side&amp;path=/branches/python3/autoload/conque_subprocess.py&amp;old_path=/branches/python3/autoload/conque_subprocess.py&amp;old=234">Diff</a>
 </div>
 <pre>python 3 beginnings</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/conque/source/detail?r=236&spec=svn496';
 var publish_url = '/p/conque/source/detail?r=236&spec=svn496#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/branches/python3/autoload/conque.py');
 changed_urls.push('/p/conque/source/browse/branches/python3/autoload/conque.py?r\x3d236\x26spec\x3dsvn496');
 
 
 changed_paths.push('/branches/python3/autoload/conque_subprocess.py');
 changed_urls.push('/p/conque/source/browse/branches/python3/autoload/conque_subprocess.py?r\x3d236\x26spec\x3dsvn496');
 
 var selected_path = '/branches/python3/autoload/conque_subprocess.py';
 
 
 changed_paths.push('/branches/python3/autoload/conque_term.vim');
 changed_urls.push('/p/conque/source/browse/branches/python3/autoload/conque_term.vim?r\x3d236\x26spec\x3dsvn496');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/conque/source/browse/branches/python3/autoload/conque.py?r=236&amp;spec=svn496"
 
 >...nches/python3/autoload/conque.py</option>
 
 <option value="/p/conque/source/browse/branches/python3/autoload/conque_subprocess.py?r=236&amp;spec=svn496"
 selected="selected"
 >...n3/autoload/conque_subprocess.py</option>
 
 <option value="/p/conque/source/browse/branches/python3/autoload/conque_term.vim?r=236&amp;spec=svn496"
 
 >...python3/autoload/conque_term.vim</option>
 
 </select>
 </td></tr></table>
 
 
 



 <div style="white-space:nowrap">
 Project members,
 <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fconque%2Fsource%2Fbrowse%2Fbranches%2Fpython3%2Fautoload%2Fconque_subprocess.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fconque%2Fsource%2Fbrowse%2Fbranches%2Fpython3%2Fautoload%2Fconque_subprocess.py"
 >sign in</a> to write a code review</div>


 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/conque/source/detail?spec=svn496&r=234">r234</a>
 by nicoraffo
 on Jul 20, 2010
 &nbsp; <a href="/p/conque/source/diff?spec=svn496&r=234&amp;format=side&amp;path=/branches/python3/autoload/conque_subprocess.py&amp;old_path=/trunk/autoload/conque_subprocess.py&amp;old=159">Diff</a>
 <br>
 <pre class="ifOpened">python3 branch</pre>
 </div>
 
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/conque/source/detail?spec=svn496&r=159">r159</a>
 by nicoraffo
 on Jan 31, 2010
 &nbsp; <a href="/p/conque/source/diff?spec=svn496&r=159&amp;format=side&amp;path=/trunk/autoload/conque_subprocess.py&amp;old_path=/trunk/plugin/conque_subprocess.py&amp;old=158">Diff</a>
 <br>
 <pre class="ifOpened">move files around</pre>
 </div>
 
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/conque/source/detail?spec=svn496&r=158">r158</a>
 by nicoraffo
 on Jan 31, 2010
 &nbsp; <a href="/p/conque/source/diff?spec=svn496&r=158&amp;format=side&amp;path=/trunk/plugin/conque_subprocess.py&amp;old_path=/trunk/conque/plugin/conque_subprocess.py&amp;old=142">Diff</a>
 <br>
 <pre class="ifOpened">move files around</pre>
 </div>
 
 
 <a href="/p/conque/source/list?path=/branches/python3/autoload/conque_subprocess.py&start=236">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 3347 bytes,
 129 lines</div>
 
 <div><a href="//conque.googlecode.com/svn/branches/python3/autoload/conque_subprocess.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn496': '/branches/python3/autoload/conque_subprocess.py'}
 codereviews = CR_controller.setup(
 {"assetHostPath": "https://ssl.gstatic.com/codesite/ph", "token": null, "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/18133036155640238800", "domainName": null, "loggedInUserEmail": null, "relativeBaseUrl": "", "profileUrl": null, "projectName": "conque", "projectHomeUrl": "/p/conque"}, '', 'svn496', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/18133036155640238800/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

