import sublime, sublime_plugin, webbrowser

class JqueryDocsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        def clean_up(text, listing):
            for value in listing:
                text = text.replace(value, '')
            return text

        # get current user selection
        replaceables = ["(", ")", "{", "}", ";", ".", "$"]
        keyword = clean_up(self.view.substr(self.view.sel()[0]), replaceables)

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
        if not keyword:
            sublime.status_message("Opening jQuery Docs. Check your Browser :)")
        else:
            sublime.status_message("Opening jQuery Docs for: \"" + keyword + "\". Check your Browser :)")

        webbrowser.open_new("http://api.jquery.com/" + keyword)
