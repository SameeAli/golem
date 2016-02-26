
class BankOfDeposit:
    # https://chriseth.github.io/browser-solidity/?gist=ac140b941584ca36be92
    INIT_HEX = "606060405261031f806100126000396000f3606060405236156100555760e060020a6000350462f714ce81146100575780633f883dfb146100de57806370a082311461015b57806390a2005b14610181578063b69ef8a814610224578063d0e30db014610242575b005b610055600435602435600160a060020a033316600090815260208190526040812054908382106100d8578290600160a060020a03821614156100965750335b600160a060020a038116600085606082818181858883f19350505050156100d85760406000908120600160a060020a0333168252602091909152805485900390555b50505050565b61005560048035602481019101353460008080805b8584101561012a578686858181101561000257602002600435016024013594508493505060a060020a8304915050848111156102c0575b600085111561015257600160a060020a03331660009081526020819052604090208054860190555b50505050505050565b600435600160a060020a03166000908152602081905260409020545b6060908152602090f35b610055602460048035918201910135600160a060020a03331660009081526020819052604081205490348201908080805b868410156101e9578787858181101561000257602002600435016024013594508493505060a060020a830491505084811115610265575b858514151561021a57846000600050600033600160a060020a03168152602001908152602001600020600050819055505b5050505050505050565b33600160a060020a0316600090815260208190526040902054610177565b610055600160a060020a0333166000908152602081905260409020805434019055565b600160a060020a038281166000818152604090208054840190556060838152968390039690913316907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef90602090a3600193909301926101b2565b600160a060020a038281166000818152602081815260409091208054850190556060848152978490039791923316917fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9190a3600193909301926100f356"  # noqa
    ABI = '[{"constant":false,"inputs":[{"name":"value","type":"uint256"},{"name":"to","type":"address"}],"name":"withdraw","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"payments","type":"bytes32[]"}],"name":"transferExternalValue","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"addr","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"payments","type":"bytes32[]"}],"name":"transfer","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"balance","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'  # noqa