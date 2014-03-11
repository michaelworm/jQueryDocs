import sublime, sublime_plugin, webbrowser

class JqueryDocsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get current user selection
        keyword = self.view.substr(self.view.sel()[0]).replace('(', '').replace(')', '').replace(';', '').replace('.', '') # make this better

        # define which keyword needs additional "jQuery." param appended
        # not included yet: jQuery.fn.extend, jQuery.fx.interval, jQuery.fx.off
        jquery_prefix = [
            "ajax", "ajaxPrefilter", "ajaxSetup", "ajaxTransport",
            "boxModel", "browser",
            "Callbacks", "contains", "cssHooks",
            "data", "Deferred", "dequeue",
            "each", "error", "extend",
            "get", "getJSON", "getScript", "globalEval", "grep",
            "hasData", "holdReady",
            "inArray", "isArray", "isEmptyObject", "isFunction", "isNumeric", "isPlainObject", "isWindow", "isXMLDoc",
            "makeArray", "map", "merge",
            "noConflict", "noop", "now",
            "param", "parseHTML", "parseJSON", "parseXML", "post", "proxy",
            "queue",
            "removeData",
            "sub", "support",
            "trim", "type",
            "unique",
            "when"
        ]

        # iterate over jquery_prefix list and append "jQuery." to the keyword
        for value in jquery_prefix:
            if keyword == value:
                keyword = "jQuery." + keyword

        # open jQuery Docs in Browser and print a message to the user
        webbrowser.open_new("http://api.jquery.com/" + keyword)
        sublime.status_message("Opening jQuery Docs for: \"" + keyword + "\". Check your Browser :)")