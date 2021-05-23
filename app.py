from dash import Dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from web3 import Web3
from smart_contract_dets import contractABI, contractAddress


# ==================== Setup connection with the blockchain & contract ====================
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

web3.eth.defaultAccount = web3.eth.accounts[0]

contract = web3.eth.contract(
    address=web3.toChecksumAddress(contractAddress), 
    abi=contractABI)


# ==================== Set initial participants accounts ====================
client1 = web3.eth.accounts[1]
client2 = web3.eth.accounts[2]

business1 = web3.eth.accounts[3]
business2 = web3.eth.accounts[4]



# ==================== Setup app layout ====================
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
        html.H1("Reward Token Dashboard", style={'margin-top': '20px'}),
        html.Hr(),
        html.Br(),

        dbc.Card([
            dbc.CardHeader(
                dbc.Tabs([
                    dbc.Tab(label="Owner", tab_id="tab1"),
                    dbc.Tab(label="Client", tab_id="tab2"),
                    dbc.Tab(label="Business", tab_id="tab3"),
                ],
                id="tabs",
                card=True,
                active_tab="tab1",
                )
            ),
                dbc.CardBody([
                    html.P(id='balance_desc', style={'text-align': 'center'}),
                    html.H1(id='total_count', style={'text-align': 'center'}),
                    # dbc.Button("refresh", id='refresh_button', color="primary", block=True, size="sm")
                ]
            , style={'margin-top': '15px'}),

            dbc.CardBody(id="card-content"),
        ])
    ])


reg_form = dbc.Form([
            dbc.FormGroup([
                dbc.Label("Address", className="mr-2"),
                dbc.Input(id='reg_addr', placeholder="Input participant address", style={"width": 500, 'margin-right': '15px'}),
            ]),
            dbc.FormGroup([
                dbc.Label("Participant Type", html_for="dropdown", className="mr-2"),
                dcc.Dropdown(
                    id="reg_dropdown",
                    options=[
                        {"label": "CLIENT", "value": 1},
                        {"label": "BUSINESS", "value": 2},
                    ], 
                    style={"width": 150 }
                ),
            ]),
        ],
    inline=True,
    style={'margin-bottom': '15px'}
    )
    

balance_query_form = dbc.Form([
                        dbc.FormGroup([
                            dbc.Label("Address", className="mr-2"),
                            dbc.Input(id='bal_addr', placeholder="Input participant address", style={"width": 500, 'margin-right': '15px'}),
                        ])
                    ],
                    inline=True,
                    style={'margin-bottom': '15px'}
                    )


issue_token_form = dbc.Form([
                        dbc.FormGroup([
                            dbc.Label("Address", className="mr-2"),
                            dbc.Input(id='issue_addr', placeholder="Input participant address", style={"width": 500, 'margin-right': '15px'}),
                        ]),
                        dbc.FormGroup([
                            dbc.Label("Amount", className="mr-2"),
                            dbc.Input(id='issue_amt', placeholder="Input token amount", style={"width": 200, 'margin-right': '15px'}),
                        ]),
                    ],
                    inline=True,
                    style={'margin-bottom': '15px'}
                    )


tab1_content = dbc.Container([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Register New Participants", style={'margin-bottom': '15px'}),
                        reg_form,
                        dbc.Button("Register", id='reg_btn', color="primary", size="sm", block=True),
                        html.P(id='reg_output'),
                        ])
                , style={'margin-top': '15px'}),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Issue Reward Token", style={'margin-bottom': '15px'}),
                        issue_token_form,
                        dbc.Button("Issue", id='issue_btn', color="primary", size="sm", block=True),
                        html.P(id='issue_output'),
                        ])
                , style={'margin-top': '15px'}),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Check Balance", style={'margin-bottom': '15px'}),
                        balance_query_form,
                        dbc.Button("Submit", id='bal_btn', color="primary", size="sm", block=True),
                        html.H4(id='bal_output'),
                        ])
                , style={'margin-top': '15px'}),
                ])


transfer_form = dbc.Form([
                        dbc.FormGroup([
                            dbc.Label("Address", className="mr-2"),
                            dbc.Input(id='transfer_addr', placeholder="Input receiver address", style={"width": 500, 'margin-right': '15px'}),
                        ]),
                        dbc.FormGroup([
                            dbc.Label("Amount", className="mr-2"),
                            dbc.Input(id='transfer_amt', placeholder="Input token amount", style={"width": 200, 'margin-right': '15px'}),
                        ]),
                    ],
                    inline=True,
                    style={'margin-bottom': '15px'}
                    )

tab2_content = dbc.Container([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Deals", style={'margin-bottom': '15px'}),
                        dbc.Button("Buy Product X from Business1 & earn 100 Reward Tokens", id='deal_btn', color="primary", size="sm",),
                        html.P(id='deal_output'),
                        ])
                , style={'margin-top': '15px'}),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Redeem", style={'margin-bottom': '15px'}),
                        dbc.Button("Redeem 5% discount from Business1 for 100 RT", id='redeem_btn', color="primary", size="sm"),
                        html.P(id='redeem_output'),
                        ])
                , style={'margin-top': '15px'}),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Transfer Reward Tokens", style={'margin-bottom': '15px'}),
                        transfer_form,
                        dbc.Button("Transfer", id='transfer_btn', color="primary", size="sm"),
                        html.P(id='transfer_output'),
                        ])
                , style={'margin-top': '15px'}),
                ])


return_form = dbc.Form([
                        dbc.FormGroup([
                            dbc.Label("Amount", className="mr-2"),
                            dbc.Input(id='return_amt', placeholder="Input amount to return", style={"width": 300, 'margin-right': '15px'}),
                        ]),
                    ],
                    inline=True,
                    style={'margin-bottom': '15px'}
                    )

tab3_content = dbc.Container([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Return Reward Tokens", style={'margin-bottom': '15px'}),
                        return_form,
                        dbc.Button("Return", id='return_btn', color="primary", size="sm"),
                        html.P(id='return_output'),
                        ])
                , style={'margin-top': '15px'}),
                ])




# ==================== Callbacks for blockhain interactions ====================

tab_contents = {
    'tab1' : tab1_content,
    'tab2' : tab2_content,
    'tab3' : tab3_content,
}

tab_to_desc = {
    'tab1' : 'Total Reward Tokens issued',
    'tab2' : "Total Reward Tokens earned",
    'tab3' : "Total Reward Tokens collected",
}


@app.callback(
    [Output("card-content", "children"),
    Output('balance_desc', 'children'),
    Output('total_count', 'children')],
    [Input("tabs", "active_tab")]
)
def tab_content(active_tab):
    # func to get respective tab contents

    tab_to_balance = {
        'tab1' : contract.functions.getTotalRewardsIssued().call(),
        'tab2' : contract.functions.getBalanceFor(client1).call(),
        'tab3' : contract.functions.getBalanceFor(business1).call(),
    }
    return tab_contents.get(active_tab), tab_to_desc.get(active_tab), tab_to_balance.get(active_tab)


def get_type(idx):
    return {1:"CLIENT", 2:"BUSINESS"}.get(idx, 'NONE')

@app.callback(
    Output("reg_output", "children"), 
    [Input("reg_addr", "value"), Input("reg_dropdown", "value"), Input("reg_btn", 'n_clicks')])
def register_particicpant(addr, _type, clicked):
    # func to register new participants
    if addr and _type and clicked:
        try:
            tx_hash = contract.functions.registerParticipant(addr, _type).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)

            return f'Addr: {addr} has been added to the platform as a {get_type(_type)}'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output("bal_output", "children"), 
    [Input("bal_addr", "value"), Input("bal_btn", 'n_clicks')])
def get_balance(addr, clicked):
    # func to get balance of input addr
    if addr and clicked:
        try:
            bal = contract.functions.getBalanceFor(addr).call()
            return f'Balance: {str(bal)}'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output("issue_output", "children"), 
    [Input("issue_addr", "value"), 
    Input("issue_amt", "value"), 
    Input("issue_btn", 'n_clicks')])
def issue_rewards(addr, amt, clicked):
    # func to issue reward tokens to given addr 
    if clicked:
        try:
            tx_hash = contract.functions.issueRewards(addr, int(amt)).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            return f'Issued {amt} Reward Tokens to {addr}'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output('deal_output', 'children'), 
    [Input("deal_btn", 'n_clicks')])
def deal_rewards(clicked):
    # func to earn reward tokens based on deals
    if clicked:
        try:
            tx_hash = contract.functions.issueRewards(client1, 100).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)
            return f'Earned 100 Reward Tokens!'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output('redeem_output', 'children'), 
    [Input("redeem_btn", 'n_clicks')])
def redeem_rewards(clicked):
    # func to redeem offers for clients
    if clicked:
        try:
            web3.eth.defaultAccount = client1

            tx_hash = contract.functions.transferP2P(business1, 100).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)

            web3.eth.defaultAccount = web3.eth.accounts[0]
            return f'Redeemed 100 Reward Tokens!'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output("transfer_output", "children"), 
    [Input("transfer_addr", "value"), 
    Input("transfer_amt", "value"), 
    Input("transfer_btn", 'n_clicks')])
def share_rewards(addr, amt, clicked):
    # func to transfer reward tokens among the participants
    if clicked:
        try:
            web3.eth.defaultAccount = client1

            tx_hash = contract.functions.transferP2P(addr, int(amt)).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)

            web3.eth.defaultAccount = web3.eth.accounts[0]
            return f'Shared {amt} Reward Tokens with {addr}!'
        except Exception as ex:
            return f'{ex}'


@app.callback(
    Output('return_output', 'children'), 
    [Input("return_amt", "value"),Input("return_btn", 'n_clicks')])
def return_rewards(amt, clicked):
    # func to return the reward tokens back to the owner
    if clicked:
        try:
            web3.eth.defaultAccount = business1

            tx_hash = contract.functions.returnRewards(int(amt)).transact()
            web3.eth.waitForTransactionReceipt(tx_hash)

            web3.eth.defaultAccount = web3.eth.accounts[0]
            return f'Returned {amt} Reward Tokens to Merchant!'
        except Exception as ex:
            return f'{ex}'
        


# ==================== Run the app server ====================
if __name__ == '__main__':
    app.run_server(use_reloader=True)
