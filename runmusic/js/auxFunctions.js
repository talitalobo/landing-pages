function ControllerLista($scope) {
    $scope.itens = [
        {produto: 'Leite', quantidade: 2, comprado: false},
        {produto: 'Cerveja', quantidade: 43, comprado: true}
    ];
    
    $scope.addItem = function() {
        $scope.itens.push({produto: $scope.item.produto,
                          quantidade: $scope.item.quantidade,
                          comprado: false});
        $scope.item.produto = $scope.item.quantidade = '';
    }
}