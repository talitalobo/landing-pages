/* os controllers são responsáveis por gerenciar os dados do aplicativo */

app.controller('MainPtController', ['$scope', function($scope) { 
  $scope.title = 'RunMusic'; 
  $scope.subtitle = 'Corra. Contemple. Renove-se.';
  $scope.subtitle2 = 'RunMusic vai além do exercício físico para oferecer o melhor da junção entre música e corrida, sintonizando a melhor batida para cada momento da atividade.';
}]);

app.controller('MenuPtController', ['$scope', function($scope) {
    $scope.login = 'LOGIN';
    $scope.runmusic = 'RUNMUSIC-SE';
    $scope.parceiros = 'PARCEIROS';
    $scope.midia = 'MÍDIA';
    $scope.contato = 'CONTATO';
    $scope.time = 'TIME';
}]);


app.controller('LetsRunPt', ['$scope', function($scope) {
    $scope.title = 'Lets Run!';
    $scope.text1 = 'Não é impressão: muita gente começou a correr pelas ruas do Brasil. Só em São Paulo o número de inscritos em provas oficiais dobrou em seis anos.';
}]);

app.controller('RunMusicPtController', ['$scope', function($scope) {
    $scope.title = 'RunMusic-se!';
    $scope.top1 = 'Corra';
    $scope.text1 = 'Corra';
    $scope.top2 = 'Aproveite';
    $scope.text2 = 'Aproveite';
    $scope.top3 = 'Acompanhe seu desempenho';
    $scope.text3 = 'Acompanhe seu desempenho';
    $scope.top4 = 'Compartilhe';
    $scope.text4 = 'Compartilhe';
}]);

app.controller('ParceirosPtController', ['$scope', function($scope) {
    $scope.labanalytics = 'Laboratório Analytics';
    $scope.farmdias = 'Farmácia Dias';
    $scope.korpus = 'Academia Korpus';
    $scope.sabor = 'Sabor e Requinte Delicatessen';
    $scope.foodjampa = 'FoodJampa';
    $scope.francy = 'Francy Cópias e ControlP';
 }]);

