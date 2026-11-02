import torch
from torch import nn

class ModuleIA(nn.Module):
    def __init__ (self):
        super().__init__()
    
    #Methode permettant d'entrainer le modèle
    def train(self, donnees_entrainement: DataLoader, loss_func: function, optimizer):

        size = len(donnes_entrainement.dataset)
        modele.train()
        for batch, (X, y) in enumerate(donnes_entrainement):
            X, y = X.to(device), y.to(device)

            # Verifie si la prediction du modèle est fausse
            pred = modele(X)
            loss = loss_func(pred, y)

            # Backpropagation
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            if batch % 100 == 0:
                loss, current = loss.item(), (batch + 1) * len(X)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    #Methode pour teste le modèle
    @staticmethode
    def test():
        pass



