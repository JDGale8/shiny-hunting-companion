if __name__ == '__main__':
    import sys
    from bin import app as GUI

    app = GUI.run()
    instance = GUI.ShinyGUI()
    sys.exit(app.exec_())
