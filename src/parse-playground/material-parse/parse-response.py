
from bs4 import BeautifulSoup

response = """<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>Course: Programming with Python</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, Course: Programming with Python" />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"iJftU1dxbb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"core_completion":{"name":"core_completion","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/course\/completion.js"},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/essential/style/course_custom.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-course-view-topcoll"
    class="format-topcoll  path-course path-course-view dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-course course-5922 context-726621 category-879 desktopdevice pagewidthnormal categoryicons modeditingmenu zoomin two-column  has-region-filter used-region-filter has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=iJftU1dxbb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=iJftU1dxbb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                    <ul class="nav">
                                        <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown"
                                                title="This course"><i class="fa fa-book"></i>This
                                                course<i class="fa fa-caret-right"></i></a>
                                            <ul class="dropdown-menu">
                                                <li><a title="People"
                                                        href="https://mydy.dypatil.edu/rait/user/index.php?id=5922"><i class="fa fa-users"></i>People</a>
                                                <li><a title="Grades"
                                                        href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5922"><i class="fa fa-list-alt icon"></i>Grades</a>
                                                <li><a
                                                        href="https://mydy.dypatil.edu/rait/mod/flexpaper/index.php?id=5922"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/flexpaper/1709815567/icon" class="icon" alt="" />Files</a>
                                                <li><a
                                                        href="https://mydy.dypatil.edu/rait/mod/presentation/index.php?id=5922"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/presentation/1709815567/icon" class="icon" alt="" />Files</a>
                                            </ul>
                                    </ul>
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Programming with Python"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">CAC404-22-A-AIML</a></li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <aside id="block-region-filter" class="span3 desktop-first-column block-region"
                                data-blockregion="filter" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip
                                    Filters</a>
                                <div id="inst9772" class="block_activities_list  block" role="complementary"
                                    data-block="activities_list" data-instanceid="9772"
                                    aria-labelledby="instance-9772-header" data-dockable="1">
                                    <div class="header">
                                        <div class="title">
                                            <div class="block_action"></div>
                                            <h2 id="instance-9772-header">Filters</h2>
                                        </div>
                                    </div>
                                    <div class="content">
                                        <ul class="accesslinks">
                                            <li class="active"><a href="#" onclick="return normal()">Lecture plans</a>
                                            </li>
                                            <li><a href="#"
                                                    onclick="return get_categories('flexpaper_presentation', 0, 5922)">Presentation</a>
                                            </li>
                                            <li><a href="#" onclick="return get_categories('casestudy', 0, 5922)">Case
                                                    study</a></li>
                                            <li><a href="#" onclick="return get_categories('forum', 0, 5922)">Discussion
                                                    forum</a></li>
                                            <li><a href="#"
                                                    onclick="return get_categories('url_page_resource', 2, 5922)">Reading
                                                    material</a></li>
                                            <li><a href="#"
                                                    onclick="return get_categories('url_opencast', 1, 5922)">Videos</a>
                                            </li>
                                            <li><a href="#"
                                                    onclick="return get_categories('assign', 0, 5922)">Assignments</a>
                                            </li>
                                            <li><a href="#"
                                                    onclick="return get_categories('dyquestion', 0, 5922)">Question
                                                    bank</a></li>
                                            <li><a href="#"
                                                    onclick="return get_categories('questionpaper', 0, 5922)">Question
                                                    paper</a></li>
                                            <li><a href="#" onclick="return get_categories('quiz', 0, 5922)">Quiz</a>
                                            </li>
                                        </ul>
                                    </div>
                                </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-2"
                                    class="skip-block">Skip Course Progress</a>
                                <div id="inst50217" class="block_course_progress  block" role="complementary"
                                    data-block="course_progress" data-instanceid="50217"
                                    aria-labelledby="instance-50217-header" data-dockable="1">
                                    <div class="header">
                                        <div class="title">
                                            <div class="block_action"></div>
                                            <h2 id="instance-50217-header">Course Progress</h2>
                                        </div>
                                    </div>
                                    <div class="content"><a
                                            href="https://mydy.dypatil.edu/rait/course/customview.php?id=5922">
                                            <div class="c100 p100 green" title="9 out of 9 activities are completed.">
                                                <span>100%</span>
                                                <div class="slice">
                                                    <div class="bar"></div>
                                                    <div class="fill"></div>
                                                </div>
                                            </div>
                                        </a>
                                        <div class="text_pending">
                                            <p><span>Total: </span>9</p>
                                            <p><span>Not Viewed: </span>0</p>
                                            <p><span>Viewed: </span>9</p>
                                        </div>
                                    </div>
                                </div><span id="sb-2" class="skip-block-to"></span>
                            </aside>
                            <div class="row-fluid span9 pull-right">
                                <h1 class="coursetitle">Programming with Python</h1>
                                <div class="box generalbox"></div>
                                <div class="bor"></div>
                                <div role="main"><span id="maincontent"></span>
                                    <form action="." method="get">
                                        <div><input type="hidden" id="completion_dynamic_change" name="completion_dynamic_change" value="0" />
                                        </div>
                                    </form>
                                    <div class="course-content">
                                        <style type="text/css" media="screen">
                                            /* <![CDATA[ */

                                            /* -- Toggle -- */
                                            .course-content ul.ctopics li.section .content .toggle,
                                            .course-content ul.ctopics li.section .content.sectionhidden {
                                                background-color: #e2e2f2;
                                            }

                                            /* -- Toggle text -- */
                                            .course-content ul.ctopics li.section .content .toggle a,
                                            .course-content ul.ctopics li.section .content.sectionhidden {
                                                color: #000000;
                                                text-align: left;
                                            }

                                            /* Toggle icon position. */
                                            .course-content ul.ctopics li.section .content .toggle a,
                                            #toggle-all .content h4 a {
                                                background-position: right center;
                                            }

                                            /* -- What happens when a toggle is hovered over -- */
                                            .course-content ul.ctopics li.section .content .toggle a:hover,
                                            .course-content ul.ctopics li.section .content.sectionhidden .toggle a:hover {
                                                color: #888888;
                                            }

                                            .course-content ul.ctopics li.section .content div.toggle:hover {
                                                background-color: #eeeeff;
                                            }

                                            .course-content ul.ctopics li.section.main .content,
                                            .course-content ul.ctopics li.tcsection .content {
                                                margin: 0 28px;
                                            }

                                            .course-content ul.ctopics li.section.main .side,
                                            .course-content ul.ctopics li.tcsection .side {
                                                width: 28px;
                                            }

                                            .course-content ul.ctopics li.section {
                                                display: inline-block;
                                                vertical-align: top;
                                            }

                                            .course-content ul.ctopics li.section.hidden {
                                                display: inline-block !important;
                                                /* Only using '!important' because of Bootstrap 3. */
                                            }

                                            body.ie7 .course-content ul.ctopics li.section {
                                                zoom: 1;
                                                *display: inline;
                                            }

                                            .course-content ul.ctopics li.section .content .toggle,
                                            .course-content ul.ctopics li.section .content.sectionhidden {
                                                -moz-border-top-left-radius: 0.7em;
                                                -webkit-border-top-left-radius: 0.7em;
                                                border-top-left-radius: 0.7em;
                                                -moz-border-top-right-radius: 0.7em;
                                                -webkit-border-top-right-radius: 0.7em;
                                                border-top-right-radius: 0.7em;
                                                -moz-border-bottom-right-radius: 0.7em;
                                                -webkit-border-bottom-right-radius: 0.7em;
                                                border-bottom-right-radius: 0.7em;
                                                -moz-border-bottom-left-radius: 0.7em;
                                                -webkit-border-bottom-left-radius: 0.7em;
                                                border-bottom-left-radius: 0.7em;
                                            }

                                            /* ]]> */
                                        </style>
                                        <div id="completionprogressid" class="completionprogress">Your
                                            progress<span class="helptooltip"><a href="https://mydy.dypatil.edu/rait/help.php?component=completion&amp;identifier=completionicons&amp;lang=en" title="Help with Completion tick boxes" aria-haspopup="true" target="_blank"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/help" alt="Help with Completion tick boxes" class="iconhelp" /></a></span>
                                        </div>
                                        <h2 class="accesshide">Week</h2>
                                        <ul class="ctopics">
                                            <li class="tcsection main clearfix" id="toggle-all">
                                                <div class="left side"><img width="1" height="1" class="spacer" alt="" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/spacer" />
                                                </div>
                                                <div class="right side"><img width="1" height="1" class="spacer" alt="" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/spacer" />
                                                </div>
                                                <div class="content">
                                                    <div class="sectionbody toggle-point-hover toggle-point">
                                                        <h4><span id='specialstring'>Contents & Assignments</span><a
                                                                class="on tc-small" href="#"
                                                                id="toggles-all-opened">Open all</a><a
                                                                class="off tc-small" href="#"
                                                                id="toggles-all-closed">Close all</a></h4>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="tcsection main clearfix" id="topcoll-display-instructions">
                                                <div class="left side"><img width="1" height="1" class="spacer" alt="" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/spacer" />
                                                </div>
                                                <div class="right side"><img width="1" height="1" class="spacer" alt="" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/spacer" />
                                                </div>
                                                <div class="content">
                                                    <div class="sectionbody">
                                                        <p class="topcoll-display-instructions">Instructions: Clicking
                                                            on the section name will show / hide the section.</p>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                        <ul class="ctopics topics ctlayout" style="width:100%; padding:0px;">
                                            <li id="section-1" class="section main clearfix" role="region"
                                                aria-label="Week 1" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-1"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 1</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-1">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-611990">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=611990"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 1 ppython_uw<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="611990" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 1 ppython_uw" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 1 ppython_uw. Select to mark as complete." title="Mark as complete: week 1 ppython_uw" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 11/01/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-2" class="section main clearfix" role="region"
                                                aria-label="Week 2" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-2"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 2</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-2">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-611991">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=611991"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 2 ppython_uw<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="611991" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 2 ppython_uw" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 2 ppython_uw. Select to mark as complete." title="Mark as complete: week 2 ppython_uw" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 15/01/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 16/01/2024,
                                                            09:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 18/01/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-3" class="section main clearfix" role="region"
                                                aria-label="Week 3" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-3"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 3</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-3">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-611992">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=611992"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 3 ppython_uw<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="611992" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 3 ppython_uw" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 3 ppython_uw. Select to mark as complete." title="Mark as complete: week 3 ppython_uw" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 23/01/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 29/01/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-4" class="section main clearfix" role="region"
                                                aria-label="Week 4" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-4"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 4</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-4">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-612128">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=612128"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 4 ppython_uw<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="612128" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 4 ppython_uw" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 4 ppython_uw. Select to mark as complete." title="Mark as complete: week 4 ppython_uw" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 30/01/2024,
                                                            09:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-5" class="section main clearfix" role="region"
                                                aria-label="Week 5" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-5"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 5</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-5">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-612151">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=612151"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 5 ppython_uw<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="612151" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 5 ppython_uw" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 5 ppython_uw. Select to mark as complete." title="Mark as complete: week 5 ppython_uw" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 06/02/2024,
                                                            09:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 05/02/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 08/02/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 12/02/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 13/02/2024,
                                                            09:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-6" class="section main clearfix" role="region"
                                                aria-label="Week 6" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-6"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 6</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-6">
                                                        <ul class="section img-text">
                                                            <li class="activity flexpaper modtype_flexpaper "
                                                                id="module-613117">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/flexpaper/view.php?id=613117"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 6 ppython_uw_ projects<span class="accesshide " > Presentation (Secured PDF)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="613117" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 6 ppython_uw_ projects" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 6 ppython_uw_ projects. Select to mark as complete." title="Mark as complete: week 6 ppython_uw_ projects" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 15/02/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 29/02/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 05/03/2024,
                                                            09:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 07/03/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 07/03/2024,
                                                            12:00 pm</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 11/03/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 12/03/2024,
                                                            09:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 01/04/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-7" class="section main clearfix" role="region"
                                                aria-label="Week 7" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-7"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 7</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-7">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-613116">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=613116"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 7 ppython_uw_try except_file handling<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="613116" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 7 ppython_uw_try except_file handling" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 7 ppython_uw_try except_file handling. Select to mark as complete." title="Mark as complete: week 7 ppython_uw_try except_file handling" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 02/04/2024,
                                                            09:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-8" class="section main clearfix" role="region"
                                                aria-label="Week 8" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-8"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 8</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-8">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-614269">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=614269"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 8 ppython_uw_Tkinter<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="614269" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 8 ppython_uw_Tkinter" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 8 ppython_uw_Tkinter. Select to mark as complete." title="Mark as complete: week 8 ppython_uw_Tkinter" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 04/04/2024,
                                                            11:00 am</p>
                                                        <p style="color: #000;margin: 0px;">Attendance: 15/04/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-9" class="section main clearfix" role="region"
                                                aria-label="Week 9" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-9"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 9</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-9">
                                                        <ul class="section img-text">
                                                            <li class="activity presentation modtype_presentation "
                                                                id="module-614437">
                                                                <div>
                                                                    <div class="mod-indent-outer">
                                                                        <div class="mod-indent"></div>
                                                                        <div>
                                                                            <div class="activityinstance"><a class=""
                                                                                    onclick=""
                                                                                    href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=614437"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/f/pdf-24" class="iconlarge activityicon" alt=" " role="presentation" /><span class="instancename">week 9 ppython  pandas_numpy_matplotlib_regression<span class="accesshide " > Presentation (Download)</span></span></a>
                                                                            </div>
                                                                            <span class="actions"><form method="post" action="https://mydy.dypatil.edu/rait/course/togglecompletion.php" class="togglecompletion"><div><input type="hidden" name="id" value="614437" /><input type="hidden" name="sesskey" value="iJftU1dxbb" /><input type="hidden" name="modulename" value="week 9 ppython  pandas_numpy_matplotlib_regression" /><input type="hidden" name="completionstate" value="1" /><input type="image" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/completion-manual-n" alt="Not completed: week 9 ppython  pandas_numpy_matplotlib_regression. Select to mark as complete." title="Mark as complete: week 9 ppython  pandas_numpy_matplotlib_regression" aria-live="polite" /></div></form></span>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 18/04/2024,
                                                            11:00 am</p>
                                                    </div>
                                                </div>
                                            </li>
                                            <li id="section-10" class="section main clearfix" role="region"
                                                aria-label="Week 10" style="width:100%;">
                                                <div class="left side"></div>
                                                <div class="sectionrightcontent">Faculty: Uttam Waghmode</div>
                                                <div class="content">
                                                    <div class="sectionhead toggle toggle-point" id="toggle-10"><a
                                                            class="toggle_open the_toggle tc-small"
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">
                                                            <h3>Week 10</h3>
                                                        </a></div>
                                                    <div class="sectionbody toggledsection sectionopen"
                                                        id="toggledsection-10">
                                                        <ul class="section img-text"></ul>
                                                        <p style="color: #000;margin: 0px;">Attendance: 24/04/2024,
                                                            01:00 pm</p>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                        <div id="filterlist"></div>
                                        <div id="popupdiv"></div>
                                        <script type="text/javascript">
                                            function normal() {
        //code
        $('.ctopics').show();
        $('#filterlist').hide();
        $('.sectionbody.toggle-arrow-hover.toggle-arrow.filters').hide();
        return false;
    }
    function get_categories(activity, param, courseid) {
        $('.ctopics').hide();
        $('.sectionbody.toggle-arrow-hover.toggle-arrow.filters').show();
         $('#filterlist').show();
        var instructor = $('#courseinstructor').val();
        if(!instructor){
            instructor = 0;
        }
        // alert(instructor);
        var path =  'https://mydy.dypatil.edu/rait';
        $.ajax({url:path+"/course/format/topcoll/trainings.php?activity="+activity+"&instructor="+instructor+"&param="+param+"&courseid="+courseid,
        beforeSend: function(){
           $("#filterlist").html('<div class=grid_customloading_img><img src="format/topcoll/pix/preloader.gif"></img></div>');
        },
        success:function(result){
            // var output = $.parseJSON(result);
            // alert(result);
            $("#filterlist").html(result);
            $('.on.tc-small').css("display", "none");
            $('.off.tc-small').css("display", "none");
            var i;
            for (i = 1; i < 11; i++) {
                var checkli = $("#filterlist #toggledsection-"+i).find("li").length;
                if(checkli > 0){
                    $('#filterlist #toggle-'+i+' .toggle_closed').addClass('toggle_open').removeClass('toggle_closed');
                    $('#filterlist #toggledsection-'+i).addClass('sectionopen');
                }
            }
        },
        cache: true,dataType: "html"});
        return false;
    }
var make_button_active = function()
{
  //Get item siblings
  var siblings =($(this).siblings());

  //Remove active class on all buttons
  siblings.each(function (index)
    {
      $(this).removeClass('active');
    }
  )


  //Add the clicked button class
  $(this).addClass('active');
}

//Attach events to menu
$(document).ready(
  function()
  {
    $(".accesslinks li").click(make_button_active);
  }  
)

function get_popup(param, activity, module) {
        $('#gridmiddle-column').hide();
         $('#select_course').show();
        var path =  'https://mydy.dypatil.edu/rait';
        $.ajax({url:path+"/course/format/topcoll/pop.php?activity="+activity+"&param="+param+"&module="+module,
        beforeSend: function(){
        },
        success:function(result){
            var output = $.parseJSON(result);
            $("#popupdiv").html(output);
            $("#popupdiv").dialog( {
                create: function(event, ui) {
                    var widget = $(this).dialog("widget");
                    $(".ui-dialog-titlebar-close .ui-button-text", widget).hide();
                    $(".ui-dialog-titlebar-close .ui-icon-closethick", widget).addClass("ui-icon-circle-close");
                   },
                   width: 900
                }
                );
        },
        cache: true,dataType: "html"});
        return false;
    }
    // Close Pop-in If the user clicks anywhere else on the page
jQuery('body')
    .bind('click', function(e) {
        if( !jQuery(e.target).closest('.ui-dialog').length
        ) {
            //jQuery('#popupdiv').dialog('close');
        }
    });
   // jQuery('#popupdiv').dialog('isOpen') &&
            
                                        </script>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-3" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course contains_branch" aria-expanded="true">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5922"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span><a href="#sb-7" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-7" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.yui.add_module({"format_topcoll":{"name":"format_topcoll","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/course\/format\/topcoll\/module.js","requires":[]}});

//]]>
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/course/format/topcoll/format.js"></script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"completion":{"completion-title-manual-y":"Mark as not complete: {$a}","completion-title-manual-n":"Mark as complete: {$a}","completion-alt-manual-y":"Completed: {$a}. Select to mark as not complete.","completion-alt-manual-n":"Not completed: {$a}. Select to mark as complete."},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168056","key":"168056","type":30},{"id":"expandable_branch_30_168107","key":"168107","type":30},{"id":"expandable_branch_30_168108","key":"168108","type":30},{"id":"expandable_branch_30_168109","key":"168109","type":30},{"id":"expandable_branch_30_168110","key":"168110","type":30},{"id":"expandable_branch_30_168111","key":"168111","type":30},{"id":"expandable_branch_30_168112","key":"168112","type":30},{"id":"expandable_branch_30_168113","key":"168113","type":30},{"id":"expandable_branch_30_168114","key":"168114","type":30},{"id":"expandable_branch_30_168115","key":"168115","type":30},{"id":"expandable_branch_30_168116","key":"168116","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
 M.util.js_pending('random663a539895ef41'); Y.use('core_completion', function(Y) { M.core_completion.init(Y);  M.util.js_complete('random663a539895ef41'); });
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst9772","title":"Filters","preference":"block9772hidden","tooltipVisible":"Hide Filters block","tooltipHidden":"Show Filters block"});
M.util.init_block_hider(Y, {"id":"inst50217","title":"Course Progress","preference":"block50217hidden","tooltipVisible":"Hide Course Progress block","tooltipHidden":"Show Course Progress block"});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663a539895ef48'); Y.use('format_topcoll', function(Y) { M.format_topcoll.init(Y, "5922", null, 10, 1, 0);  M.util.js_complete('random663a539895ef48'); });
 M.util.js_pending('random663a539895ef49'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663a539895ef49'); });

});
//]]>
    </script>
</body>

</html>
"""

soup = BeautifulSoup(response, 'lxml')
    
activities = soup.select(".activityinstance")

# SELECTING all anchor tags, seems to give me access to past semester and all their contents!
result = []
for activity in activities:
    soup = BeautifulSoup(str(activity), 'lxml')
    link = soup.select_one("a")
    link = link['href']
    print(link)
    
    name = soup.find("span")
    name = name.contents[0]
    
    activity_object = {
        'name':name,
        'link':link
    }
    
    result.append(activity_object)
    

print(result)




