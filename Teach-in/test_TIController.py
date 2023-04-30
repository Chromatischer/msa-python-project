import TiController
import SimpleTxtConnector
import TiView

if __name__ == "__main__":
    ftxt = SimpleTxtConnector.SimpleTxtConnector().txt
    tiv = TiView.TiView(ftxt)
    tic = TiController.TiController(ftxt, tiv, verbose=False)
    tic.run()
