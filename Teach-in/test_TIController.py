import TiController
import SimpleTxtConnector

if __name__ == "__main__":
    ftxt = SimpleTxtConnector.SimpleTxtConnector().txt
    tic = TiController.TiController(ftxt, verbose=True)
    tic.run()
