import plotly.express as px
import pandas as pd
import requests
import streamlit as st
import numpy as np
from pycoingecko import CoinGeckoAPI



# import and print latest VSO Unlock file to copy output and paste into the df variable that follows as a manually created dataframe
df1 = pd.read_csv(r'F:\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Data - VSO Unlocks Ordered 20211102.csv')
print(df1.to_dict())

# df = pd.DataFrame.from_dict({'VSO Amount': {0: 250000, 1: 250000, 2: 250000, 3: 250000, 4: 916666, 5: 916666, 6: 916666, 7: 916666, 8: 208333, 9: 208333, 10: 208333, 11: 208333, 12: 1, 13: 1, 14: 208333, 15: 208333, 16: 208333, 17: 208333, 18: 10400000, 19: 33333, 20: 33333, 21: 33333, 22: 33333, 23: 170833, 24: 16666, 25: 12500, 26: 8333, 27: 208333, 28: 250000, 29: 916666, 30: 208333, 31: 158333, 32: 791666, 33: 33333, 34: 20833, 35: 170833, 36: 16666, 37: 12500, 38: 8333, 39: 208333, 40: 250000, 41: 916666,42: 208333, 43: 158333, 44: 791666, 45: 33333, 46: 170833, 47: 16666, 48: 12500, 49: 8333, 50: 208333, 51: 250000, 52: 916666, 53: 208333, 54: 158333, 55: 791666, 56: 33333, 57: 170833, 58: 16666, 59: 12500, 60: 8333, 61: 208333, 62: 250000, 63: 916666, 64: 208333, 65: 158333, 66: 791666, 67: 33333, 68: 170833, 69: 16666, 70: 12500, 71: 8333, 72: 208333, 73: 250000, 74: 916666, 75: 208333, 76: 158333, 77: 791666, 78: 33333, 79: 170833, 80: 16666, 81: 12500, 82: 8333, 83: 208333, 84:250000, 85: 916666, 86: 208333, 87: 158333, 88: 791666, 89: 33333, 90: 170833, 91: 16666, 92: 12500, 93: 8333, 94: 208333, 95: 250000, 96: 916666, 97: 208333, 98: 158333, 99: 791666, 100: 33333, 101: 170833, 102: 16666, 103: 12500, 104: 8333, 105: 208333, 106: 250000, 107: 916666, 108: 208333, 109: 158333, 110: 3958338, 111: 33335, 112: 170833, 113: 16666, 114: 12500, 115: 8333, 116: 208333, 117: 170833, 118: 16666, 119: 12500, 120: 8333, 121: 208333, 122: 170833, 123: 16666, 124: 12500, 125: 8333, 126: 208333, 127: 170833, 128: 16666, 129: 12500, 130: 8333, 131: 208333},
#                              'Days Until Unlock': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 14, 24: 14, 25: 14, 26: 14, 27: 14, 28: 14, 29: 14, 30: 14, 31: 15, 32: 15, 33: 15, 34: 15, 35: 44, 36: 44, 37: 44, 38: 44, 39: 44, 40: 44, 41: 44, 42: 44, 43: 45, 44: 45, 45: 45, 46: 75, 47: 75, 48: 75, 49: 75, 50: 75, 79: 165, 80: 165, 81: 165, 82: 165, 83: 165, 84: 165, 85: 165, 86: 165, 87: 166, 88: 166, 89: 166, 90: 195, 91: 195, 92: 195, 93: 195, 94: 195, 95: 195, 96: 195, 97: 195, 98: 196, 99: 196, 100: 196, 101: 226, 102: 226, 103: 226, 104: 226, 105: 226, 106: 226, 107: 226, 108: 226, 109: 227, 110: 227, 111: 227, 112: 256, 113: 256, 114: 256, 115: 256, 116: 256, 117: 287, 118: 287, 119: 287, 120: 287, 121: 287, 122: 318, 123: 318, 124: 318, 125: 318, 126: 318, 127: 348, 128: 348, 129: 348, 130: 348, 131: 348},
#                              'Date of Unlock': {0: '10/17/2021', 1: '10/17/2021', 2: '10/17/2021', 3: '10/17/2021', 4: '10/17/2021', 5: '10/17/2021', 6: '10/17/2021', 7: '10/17/2021', 8: '10/17/2021', 9: '10/17/2021', 10: '10/17/2021', 11: '10/17/2021', 12: '10/17/2021', 13: '10/17/2021', 14: '10/17/2021', 15: '10/17/2021', 16: '10/17/2021', 17: '10/17/2021', 18: '10/17/2021', 19: '10/17/2021', 20: '10/17/2021', 21: '10/17/2021', 22: '10/17/2021', 23: '10/31/2021', 24: '10/31/2021', 25: '10/31/2021', 26: '10/31/2021', 27: '10/31/2021', 28: '10/31/2021', 29: '10/31/2021', 30: '10/31/2021', 31: '11/1/2021', 32: '11/1/2021', 33: '11/1/2021', 34: '11/1/2021', 35: '11/30/2021', 36: '11/30/2021', 37: '11/30/2021', 38: '11/30/2021', 39: '11/30/2021', 40: '11/30/2021', 41: '11/30/2021', 42: '11/30/2021', 43: '12/1/2021', 44: '12/1/2021', 45: '12/1/2021', 46: '12/31/2021', 47: '12/31/2021', 48: '12/31/2021', 49: '12/31/2021', 50: '12/31/2021', 51: '12/31/2021', 52: '12/31/2021', 53: '12/31/2021', 54: '1/1/2022', 55: '1/1/2022', 56: '1/1/2022', 57: '1/31/2022', 58: '1/31/2022', 59: '1/31/2022', 60: '1/31/2022', 61: '1/31/2022', 62: '1/31/2022', 63: '1/31/2022', 64: '1/31/2022', 65: '2/1/2022', 66: '2/1/2022', 67: '2/1/2022', 68: '2/28/2022', 69: '2/28/2022', 70: '2/28/2022', 71: '2/28/2022', 72: '2/28/2022', 73: '2/28/2022', 74: '2/28/2022', 75: '2/28/2022', 76: '3/1/2022', 77: '3/1/2022', 78: '3/1/2022', 79: '3/31/2022', 80: '3/31/2022', 81: '3/31/2022', 82: '3/31/2022', 83: '3/31/2022', 84: '3/31/2022', 85: '3/31/2022', 86: '3/31/2022', 87: '4/1/2022', 88: '4/1/2022', 89: '4/1/2022', 90: '4/30/2022', 91: '4/30/2022', 92: '4/30/2022', 93: '4/30/2022', 94: '4/30/2022', 95: '4/30/2022', 96: '4/30/2022', 97: '4/30/2022', 98: '5/1/2022', 99: '5/1/2022', 100: '5/1/2022', 101: '5/31/2022', 102: '5/31/2022', 103: '5/31/2022', 104: '5/31/2022', 105: '5/31/2022', 106: '5/31/2022', 107: '5/31/2022', 108: '5/31/2022', 109: '6/1/2022', 110: '6/1/2022', 111: '6/1/2022', 112: '6/30/2022', 113: '6/30/2022', 114: '6/30/2022', 115: '6/30/2022', 116: '6/30/2022', 117: '7/31/2022', 118: '7/31/2022', 119: '7/31/2022', 120: '7/31/2022', 121: '7/31/2022', 122: '8/31/2022', 123: '8/31/2022', 124: '8/31/2022', 125: '8/31/2022', 126: '8/31/2022', 127: '9/30/2022', 128: '9/30/2022', 129: '9/30/2022', 130: '9/30/2022', 131: '9/30/2022'},
#                              'Withdrawal Address': {0: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 1: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 2: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 3: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 4: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 5: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 6: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 7: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 8: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 9: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 10: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 11: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 12: '0xaE778784228B799fa9560ea24fDcda6795205F27', 13: '0x906935f4b42e632137504C0ea00D43C6442272bf', 14: '0xaE778784228B799fa9560ea24fDcda6795205F27', 15: '0xaE778784228B799fa9560ea24fDcda6795205F27', 16: '0xaE778784228B799fa9560ea24fDcda6795205F27', 17: '0xaE778784228B799fa9560ea24fDcda6795205F27', 18: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 19: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 20: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 21: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 22: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 23: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 24: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 25: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 26: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 27: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 28: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 29: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 30: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 31: '0xaE778784228B799fa9560ea24fDcda6795205F27', 32: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 33: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 34: '0xaE778784228B799fa9560ea24fDcda6795205F27', 35: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 36: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 37: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 38: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 39: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 40: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 41: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 42: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 43: '0xaE778784228B799fa9560ea24fDcda6795205F27', 44: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 45: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 46: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 47: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 48: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 49: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 50: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 51: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 52: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 53: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 54: '0xaE778784228B799fa9560ea24fDcda6795205F27', 55: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 56: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 57: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 58: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 59: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 60: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 61: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 62: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 63: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 64: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 65: '0xaE778784228B799fa9560ea24fDcda6795205F27', 66: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 67: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 68: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 69: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 70:'0xD55A5d574842E4aFff7470A60AF8343672cE6687', 71: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 72: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 73: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 74: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 75: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 76: '0xaE778784228B799fa9560ea24fDcda6795205F27', 77: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 78: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 79: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 80: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 81: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 82: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 83: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 84: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 85: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 86: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 87: '0xaE778784228B799fa9560ea24fDcda6795205F27', 88: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 89: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 90: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 91: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 92: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 93: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 94: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 95: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 96: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 97: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 98: '0xaE778784228B799fa9560ea24fDcda6795205F27', 99: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 100: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 101: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 102: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 103: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 104: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 105: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 106: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 107: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 108: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 109: '0xaE778784228B799fa9560ea24fDcda6795205F27', 110: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 111: '0x9e430dC2eDB9992E5d3917c661a4086FD77A1450', 112: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 113: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 114: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 115: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 116: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 117: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 118: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 119: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 120: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 121: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 122: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 123: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 124: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 125: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 126: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 127: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 128: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 129: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 130: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 131: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F'},
#                              'Internal or External': {0: 'External', 1:'External', 2: 'External', 3: 'External', 4: 'Internal', 5: 'Internal', 6: 'Internal', 7: 'Internal', 8: 'Internal', 9: 'Internal', 10: 'Internal', 11: 'Internal', 12: 'External', 13: 'Unknown', 14: 'External', 15: 'External', 16: 'External', 17: 'External', 18: 'Internal', 19: 'Unknown', 20: 'Unknown', 21: 'Unknown', 22: 'Unknown', 23: 'Internal', 24: 'External', 25: 'External', 26: 'External', 27: 'External', 28: 'External', 29: 'Internal', 30: 'Internal', 31: 'External', 32: 'Internal', 33: 'Unknown', 34: 'External', 35: 'Internal', 36: 'External', 37: 'External', 38: 'External', 39: 'External', 40: 'External', 41: 'Internal', 42: 'Internal', 43: 'External', 44: 'Internal', 45: 'Unknown', 46: 'Internal', 47: 'External', 48: 'External', 49: 'External', 50: 'External', 51: 'External', 52: 'Internal', 53: 'Internal', 54: 'External', 55: 'Internal', 56: 'Unknown', 57: 'Internal', 58: 'External', 59: 'External', 60: 'External', 61: 'External', 62: 'External', 63: 'Internal', 64: 'Internal', 65: 'External', 66: 'Internal', 67: 'Unknown', 68: 'Internal', 69: 'External', 70: 'External', 71: 'External', 72: 'External', 73: 'External', 74: 'Internal', 75: 'Internal', 76: 'External', 77: 'Internal', 78: 'Unknown', 79: 'Internal', 80: 'External', 81: 'External', 82: 'External', 83: 'External', 84: 'External', 85: 'Internal', 86: 'Internal', 87: 'External', 88: 'Internal', 89: 'Unknown', 90: 'Internal', 91: 'External', 92: 'External', 93: 'External', 94: 'External', 95: 'External', 96: 'Internal', 97: 'Internal', 98: 'External', 99: 'Internal', 100: 'Unknown', 101: 'Internal', 102: 'External', 103: 'External', 104: 'External', 105: 'External', 106: 'External', 107: 'Internal', 108: 'Internal', 109: 'External', 110: 'Internal', 111: 'Unknown', 112: 'Internal', 113: 'External', 114: 'External', 115: 'External', 116: 'External', 117: 'Internal', 118: 'External', 119: 'External', 120: 'External', 121: 'External', 122: 'Internal', 123: 'External', 124: 'External', 125: 'External', 126: 'External', 127: 'Internal', 128: 'External', 129: 'External', 130: 'External', 131: 'External'}})

df = pd.DataFrame.from_dict({'VSO Amount': {0: 170833, 1: 16666, 2: 12500, 3: 8333, 4: 208333, 5: 250000, 6: 250000, 7: 250000, 8: 250000, 9: 250000, 10: 916666, 11: 916666, 12: 916666, 13: 916666, 14: 916666, 15: 208333, 16: 208333, 17: 208333, 18: 208333, 19: 208333, 20: 1, 21: 1, 22: 158333, 23: 208333, 24: 208333, 25: 208333, 26: 208333, 27: 791666, 28: 10400000, 29: 33333, 30: 33333, 31: 33333, 32: 33333, 33: 33333, 34: 20833, 35: 170833, 36: 16666, 37: 12500, 38: 8333, 39: 208333, 40: 250000, 41: 916666, 42: 208333, 43: 791666, 44: 33333, 45: 158333, 46: 170833, 47: 16666, 48: 12500, 49: 8333, 50: 208333, 51: 250000, 52: 916666, 53: 208333, 54: 791666, 55: 33333, 56: 158333, 57: 170833, 58: 16666, 59: 12500, 60: 8333, 61: 208333, 62: 250000, 63: 916666, 64: 208333, 65: 791666, 66: 33333, 67: 158333, 68: 170833, 69: 16666, 70: 12500, 71: 8333, 72: 208333, 73: 250000, 74: 916666, 75: 208333, 76: 791666, 77: 33333, 78: 158333, 79: 170833, 80: 16666, 81: 12500, 82: 8333, 83: 208333, 84: 250000, 85: 916666, 86: 208333, 87: 791666, 88: 33333, 89: 158333, 90: 170833, 91: 16666, 92: 12500, 93: 8333, 94: 208333, 95: 250000, 96: 916666, 97: 208333, 98: 791666, 99: 33333, 100: 158333, 101: 170833, 102: 16666, 103: 12500, 104: 8333, 105: 208333, 106: 250000, 107: 916666, 108: 208333, 109: 3958338, 110: 33335, 111: 158333, 112: 170833, 113: 16666, 114: 12500, 115: 8333, 116: 208333, 117: 170833, 118: 16666, 119: 12500, 120: 8333, 121: 208333, 122: 170833, 123: 16666, 124: 12500, 125: 8333, 126: 208333, 127: 170833, 128: 16666, 129: 12500, 130: 8333, 131: 208333},
                             'Days Until Unlock': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 28, 36: 28, 37: 28, 38: 28, 39: 28, 40: 28, 41: 28, 42: 28, 43: 29, 44: 29, 45: 30, 46: 59, 47: 59, 48: 59, 49: 59, 50: 59, 51: 59, 52: 59, 53: 59, 54: 60, 55: 60, 56: 61, 57: 90, 58: 90, 59: 90, 60: 90, 61: 90, 62: 90, 63: 90, 64: 90, 65: 91, 66: 91, 67: 92, 68: 118, 69: 118, 70: 118, 71: 118, 72: 118, 73: 118, 74: 118, 75: 118, 76: 119, 77: 119, 78: 120, 79: 149, 80: 149, 81: 149, 82: 149, 83: 149, 84: 149, 85: 149, 86: 149, 87: 150, 88: 150, 89: 151, 90: 179, 91: 179, 92: 179, 93: 179, 94: 179, 95: 179, 96: 179, 97: 179, 98: 180, 99: 180, 100: 181, 101: 210, 102: 210, 103: 210, 104: 210, 105: 210, 106: 210, 107: 210, 108: 210, 109: 211, 110: 211, 111: 212, 112: 240, 113: 240, 114: 240, 115: 240, 116: 240, 117: 271, 118: 271, 119: 271, 120: 271, 121: 271, 122: 302, 123: 302, 124: 302, 125: 302, 126: 302, 127: 332, 128: 332, 129: 332, 130: 332, 131: 332},
                             'Date of Unlock': {0: '11/02/2021', 1: '11/02/2021', 2: '11/02/2021', 3: '11/02/2021', 4: '11/02/2021', 5: '11/02/2021', 6: '11/02/2021', 7: '11/02/2021', 8: '11/02/2021', 9: '11/02/2021', 10: '11/02/2021', 11: '11/02/2021', 12: '11/02/2021', 13: '11/02/2021', 14: '11/02/2021', 15: '11/02/2021', 16: '11/02/2021', 17: '11/02/2021', 18: '11/02/2021', 19: '11/02/2021', 20: '11/02/2021', 21: '11/02/2021', 22: '11/02/2021', 23: '11/02/2021', 24: '11/02/2021', 25: '11/02/2021', 26: '11/02/2021', 27: '11/02/2021', 28: '11/02/2021', 29: '11/02/2021', 30: '11/02/2021', 31: '11/02/2021', 32: '11/02/2021', 33: '11/02/2021', 34: '11/02/2021', 35: '11/30/2021', 36: '11/30/2021', 37: '11/30/2021', 38: '11/30/2021', 39: '11/30/2021', 40: '11/30/2021', 41: '11/30/2021', 42: '11/30/2021', 43: '12/01/2021', 44: '12/01/2021', 45: '12/02/2021', 46: '12/31/2021', 47: '12/31/2021', 48: '12/31/2021', 49: '12/31/2021', 50: '12/31/2021', 51: '12/31/2021', 52: '12/31/2021', 53: '12/31/2021', 54: '01/01/2022', 55: '01/01/2022', 56: '01/02/2022', 57: '01/31/2022', 58: '01/31/2022', 59: '01/31/2022', 60: '01/31/2022', 61: '01/31/2022', 62: '01/31/2022', 63: '01/31/2022', 64: '01/31/2022', 65: '02/01/2022', 66: '02/01/2022', 67: '02/02/2022', 68: '02/28/2022', 69: '02/28/2022', 70: '02/28/2022', 71: '02/28/2022', 72: '02/28/2022', 73: '02/28/2022', 74: '02/28/2022', 75: '02/28/2022', 76: '03/01/2022', 77: '03/01/2022', 78: '03/02/2022', 79: '03/31/2022', 80: '03/31/2022', 81: '03/31/2022', 82: '03/31/2022', 83: '03/31/2022', 84: '03/31/2022', 85: '03/31/2022', 86: '03/31/2022', 87: '04/01/2022', 88: '04/01/2022', 89: '04/02/2022', 90: '04/30/2022', 91: '04/30/2022', 92: '04/30/2022', 93: '04/30/2022', 94: '04/30/2022', 95: '04/30/2022', 96: '04/30/2022', 97: '04/30/2022', 98: '05/01/2022', 99: '05/01/2022', 100: '05/02/2022', 101: '05/31/2022', 102: '05/31/2022', 103: '05/31/2022', 104: '05/31/2022', 105: '05/31/2022', 106: '05/31/2022', 107: '05/31/2022', 108: '05/31/2022', 109: '06/01/2022', 110: '06/01/2022', 111: '06/02/2022', 112: '06/30/2022', 113: '06/30/2022', 114: '06/30/2022', 115: '06/30/2022', 116: '06/30/2022', 117: '07/31/2022', 118: '07/31/2022', 119: '07/31/2022', 120: '07/31/2022', 121: '07/31/2022', 122: '08/31/2022', 123: '08/31/2022', 124: '08/31/2022', 125: '08/31/2022', 126: '08/31/2022', 127: '09/30/2022', 128: '09/30/2022', 129: '09/30/2022', 130: '09/30/2022', 131: '09/30/2022'},
                             'Withdrawal Address': {0: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 1: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 2: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 3: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 4: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 5: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 6: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 7: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 8: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 9: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 10: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 11: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 12: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 13: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 14: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 15: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 16: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 17: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 18: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 19: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 20: '0xaE778784228B799fa9560ea24fDcda6795205F27', 21: '0x906935f4b42e632137504C0ea00D43C6442272bf', 22: '0xaE778784228B799fa9560ea24fDcda6795205F27', 23: '0xaE778784228B799fa9560ea24fDcda6795205F27', 24: '0xaE778784228B799fa9560ea24fDcda6795205F27', 25: '0xaE778784228B799fa9560ea24fDcda6795205F27', 26: '0xaE778784228B799fa9560ea24fDcda6795205F27', 27: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 28: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 29: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 30: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 31: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 32: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 33: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 34: '0xaE778784228B799fa9560ea24fDcda6795205F27', 35: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 36: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 37: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 38: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 39: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 40: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 41: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 42: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 43: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 44: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 45: '0xaE778784228B799fa9560ea24fDcda6795205F27', 46: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 47: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 48: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 49: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 50: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 51: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 52: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 53: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 54: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 55: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 56: '0xaE778784228B799fa9560ea24fDcda6795205F27', 57: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 58: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 59: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 60: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 61: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 62: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 63: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 64: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 65: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 66: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 67: '0xaE778784228B799fa9560ea24fDcda6795205F27', 68: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 69: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 70: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 71: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 72: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 73: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 74: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 75: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 76: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 77: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 78: '0xaE778784228B799fa9560ea24fDcda6795205F27', 79: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 80: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 81: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 82: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 83: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 84: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 85: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 86: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 87: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 88: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 89: '0xaE778784228B799fa9560ea24fDcda6795205F27', 90: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 91: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 92: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 93: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 94: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 95: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 96: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 97: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 98: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 99: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 100: '0xaE778784228B799fa9560ea24fDcda6795205F27', 101: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 102: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 103: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 104: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 105: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 106: '0x6c05437e3A0a6EC0379dF5A194C3ad01f1164349', 107: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 108: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 109: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 110: '0xb1bE473297660fCb4a3A92201b3E6BF788B0Ba61', 111: '0xaE778784228B799fa9560ea24fDcda6795205F27', 112: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 113: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 114: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 115: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 116: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 117: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 118: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 119: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 120: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 121: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 122: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 123: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 124: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 125: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 126: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F', 127: '0x308D2Ac1Bab7D0211717F969602fBC26D286555A', 128: '0x0fecA26DF57fA876EFd8Afd57DA52B94a04bb489', 129: '0xD55A5d574842E4aFff7470A60AF8343672cE6687', 130: '0x1f4EB1a3C7A5777b1211F760D106734159F50ACB', 131: '0x0A5E7C50eA6BB695F234e75D97D3381592B59C9F'},
                             'Internal or External': {0: 'Internal', 1: 'External', 2: 'External', 3: 'External', 4: 'External', 5: 'Internal', 6: 'Internal', 7: 'Internal', 8: 'Internal', 9: 'Internal', 10: 'Internal', 11: 'Internal', 12: 'Internal', 13: 'Internal', 14: 'Internal', 15: 'External', 16: 'External', 17: 'External', 18: 'External', 19: 'External', 20: 'External', 21: 'Unknown', 22: 'External', 23: 'External', 24: 'External', 25: 'External', 26: 'External', 27: 'Internal', 28: 'Internal', 29: 'Unknown', 30: 'Unknown', 31: 'Unknown', 32: 'Unknown', 33: 'Unknown', 34: 'External', 35: 'Internal', 36: 'External', 37: 'External', 38: 'External', 39: 'External', 40: 'Internal', 41: 'Internal', 42: 'External', 43: 'Internal', 44: 'Unknown', 45: 'External', 46: 'Internal', 47: 'External', 48: 'External', 49: 'External', 50: 'External', 51: 'Internal', 52: 'Internal', 53: 'External', 54: 'Internal', 55: 'Unknown', 56: 'External', 57: 'Internal', 58: 'External', 59: 'External', 60: 'External', 61: 'External', 62: 'Internal', 63: 'Internal', 64: 'External', 65: 'Internal', 66: 'Unknown', 67: 'External', 68: 'Internal', 69: 'External', 70: 'External', 71: 'External', 72: 'External', 73: 'Internal', 74: 'Internal', 75: 'External', 76: 'Internal', 77: 'Unknown', 78: 'External', 79: 'Internal', 80: 'External', 81: 'External', 82: 'External', 83: 'External', 84: 'Internal', 85: 'Internal', 86: 'External', 87: 'Internal', 88: 'Unknown', 89: 'External', 90: 'Internal', 91: 'External', 92: 'External', 93: 'External', 94: 'External', 95: 'Internal', 96: 'Internal', 97: 'External', 98: 'Internal', 99: 'Unknown', 100: 'External', 101: 'Internal', 102: 'External', 103: 'External', 104: 'External', 105: 'External', 106: 'Internal', 107: 'Internal', 108: 'External', 109: 'Internal', 110: 'Unknown', 111: 'External', 112: 'Internal', 113: 'External', 114: 'External', 115: 'External', 116: 'External', 117: 'Internal', 118: 'External', 119: 'External', 120: 'External', 121: 'External', 122: 'Internal', 123: 'External', 124: 'External', 125: 'External', 126: 'External', 127: 'Internal', 128: 'External', 129: 'External', 130: 'External', 131: 'External'}})

# save dataframe to file
df.to_csv(r'F:\PycharmProjects\VSO-Token-Unlocks\Manually Built Pandas DataFrame.csv', index=False)


df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])
pivot_table = df.pivot_table(index=['Date of Unlock', 'Internal or External'], values=['VSO Amount'], fill_value=0, aggfunc=np.sum)

pivot_table = df.pivot_table(index='Date of Unlock', columns='Internal or External', values='VSO Amount', aggfunc='sum', fill_value=0)

# pivot_chart = pivot_table.unstack().plot(kind='bar', stacked=True)
# st.pyplot(pivot_chart)


# explicitly create DataFrame with Unlock Schedule as of October 17th 2021 (static dataset/dataframe)
# df = pd.DataFrame.from_dict({'VSO Amount': {0: 16866662, 1: 1791664, 2: 1004165, 3: 1791664, 4: 983332, 5: 1791664, 6: 983332, 7: 1791664, 8: 983332, 9: 1791664, 10: 983332, 11: 1791664, 12: 983332, 13: 1791664, 14: 983332, 15: 1791664, 16: 4150006, 17: 416665, 18: 416665, 19: 416665, 20: 416665},
#                              'Days Until Unlock': {0: 0, 1: 14, 2: 15, 3: 44, 4: 45, 5: 75, 6: 76, 7: 106, 8: 107, 9: 134, 10: 135, 11: 165, 12: 166, 13: 195, 14: 196, 15: 226, 16: 227, 17: 256, 18: 287, 19: 318, 20: 348},
#                              'Date of Unlock': {0: '10/17/2021', 1: '10/31/2021', 2: '11/1/2021', 3: '11/30/2021', 4: '12/1/2021', 5: '12/31/2021', 6: '1/1/2022', 7: '1/31/2022', 8: '2/1/2022', 9: '2/28/2022', 10: '3/1/2022', 11: '3/31/2022', 12: '4/1/2022', 13: '4/30/2022', 14: '5/1/2022', 15: '5/31/2022', 16: '6/1/2022', 17: '6/30/2022', 18: '7/31/2022', 19: '8/31/2022', 20: '9/30/2022'},
#                              'Cumulative VSO Amount': {0: 16866662, 1: 18658326, 2: 19662491, 3: 21454155, 4: 22437487, 5: 24229151, 6: 25212483, 7: 27004147, 8: 27987479, 9: 29779143, 10: 30762475, 11: 32554139, 12: 33537471, 13: 35329135, 14: 36312467, 15: 38104131, 16: 42254137, 17: 42670802, 18: 43087467, 19: 43504132, 20: 43920797}})


# change data type of Date of Unlock Column to datetime
# df['Date of Unlock'] = pd.to_datetime(df['Date of Unlock'])


# get market data from coingecko's API and assign values to variables
url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=7d', headers={'accept':'application/json'})
# url = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=verso&order=market_cap_desc&per_page=100&page=1&sparkline=false', headers={'accept':'application/json'})
current_price = url.json()[0]['current_price']
price_change_percentage_24h = url.json()[0]['price_change_percentage_24h']
price_changepercentage_7d = url.json()[0]['price_change_percentage_7d_in_currency']
market_cap = url.json()[0]['market_cap']
circulating_supply = url.json()[0]['circulating_supply']
fdv = url.json()[0]['fully_diluted_valuation']
total_volume = url.json()[0]['total_volume']


# calling VSO and AVAX pricing data from coingecko's API directly instead of using requests and url
cg = CoinGeckoAPI()
vso_prices = cg.get_coin_market_chart_by_id(id='verso', vs_currency='usd', days=15)
avax_prices = cg.get_coin_market_chart_by_id(id='avalanche-2', vs_currency='usd', days=15)


# create date and price dataframes for each token pair
df_vso = pd.DataFrame(vso_prices['prices'], columns=['Date', 'Price'])
df_avax = pd.DataFrame(avax_prices['prices'], columns=['Date', 'Price'])
df_vso_avax = pd.DataFrame(np.array(df_vso['Price'])/np.array(df_avax['Price']), columns=['Price']) # VSO/AVAX pair


# create date-indexed df for all tokens (one token per column)
df_token_prices = pd.DataFrame({'Date': df_vso['Date'], 'VSO/USD': df_vso['Price'], 'AVAX/USD': df_avax['Price'], 'VSO/AVAX': df_vso_avax['Price']})
df_token_prices = df_token_prices.set_index('Date')
df_token_prices.index = pd.to_datetime(df_token_prices.index, unit='ms')
print(df_token_prices)


# calculate 7-day price percentage change
pd.set_option("display.max_rows", None, "display.max_columns", None)
vso_price_change_percentage_7_days = df_token_prices['VSO/USD'].pct_change()


# prepare variables for plotting later
colors = px.colors.qualitative.T10


# page layout
st.set_page_config(page_title = 'Streamlit Dashboard',
    layout='wide',
    page_icon='💹')

st.title("VSO Token Dashboard")


# market data
st.markdown("## Market Data")

first_kpi, second_kpi, third_kpi, fourth_kpi, = st.columns(4)

with first_kpi:
    st.markdown("**VSO Current Price**")
    number1 = str(current_price) + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Price Change 24h**")
    number2 = str(round(price_change_percentage_24h, 2)) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Price Change 7d**")
    number2 = str(round(price_changepercentage_7d, 2)) + '%'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Volume 24h**")
    number3 = str(f'{total_volume:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

fifth_kpi, sixth_kpi, seventh_kpi = st.columns(3)

with fifth_kpi:
    st.markdown("**Market Capitalization**")
    number3 = str(f'{market_cap:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with sixth_kpi:
    st.markdown("**Circulating Supply**")
    number4 = str(f'{int(circulating_supply):,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)

with seventh_kpi:
    st.markdown("**Fully Diluted Valuation**")
    number5 = str(f'{int(current_price * 100000000):,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number5}</h1>", unsafe_allow_html=True)


# TODO AVAX data

# plot token returns (percentage change)
st.markdown("<hr/>", unsafe_allow_html=True)


# Price Charts
st.markdown("## Price Charts")

st.markdown("### VSO/AVAX Price Chart")

newnames = {'wide_variable_0': 'VSO/USD', 'wide_variable_1': 'AVAX/USD'} # prepare newnames variable for line chart labels renaming later
fig = px.line(df_token_prices,
             x = df_token_prices.index,
             y = df_token_prices['VSO/AVAX'],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=1500
             )

st.plotly_chart(fig)


# plot token cumulative returns (cumulative percentage change)
st.markdown("### VSO and AVAX Token Returns (cumulative percentage change)")

fig2 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [(df_token_prices['VSO/USD'].pct_change()+1).cumprod(), (df_token_prices['AVAX/USD'].pct_change()+1).cumprod()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             height=800,
             width=1500
             )

fig2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig2)

# plot token returns (percentage change)
st.markdown("### VSO and AVAX Token Returns (percentage change)")

fig3 = px.line(df_token_prices,
             x = df_token_prices.index,
             y = [df_token_prices['VSO/USD'].pct_change(), df_token_prices['AVAX/USD'].pct_change()],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=1500
             )

fig3.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     ))
st.plotly_chart(fig3)


# Locked Tokens for Vesting
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Locked Tokens for Vesting")

first_kpi, second_kpi = st.columns(2)

# define variables for internal an external locked tokens
# TODO adjust static "today" date to dynamic "today"
internal_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Internal') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()
external_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'External') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()
unknown_locked = df['VSO Amount'].loc[(df['Internal or External'] == 'Unknown') &(df['Date of Unlock'] > '2021-10-17T00:00:00')].sum()

external_locked_total = external_locked + unknown_locked


with first_kpi:
    st.markdown("**Total Locked VSO - Internal Addresses**")
    number1 = str(f'{internal_locked:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Total Locked VSO - External Addresses**")
    number2 = str(f'{external_locked_total:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)


# Circulating Supply
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Circulating Supply")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


with first_kpi:
    st.markdown("**Internal Addresses**")
    number1 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**External Addresses**")
    number2 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Farms**")
    number3 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Pools**")
    number4 = 'NaN'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number4}</h1>", unsafe_allow_html=True)


# VSO Unlock Schedule
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Unlock Schedule")

st.subheader('Dataset')
st.write(df)


# TODO add cumulative back to DataFrame
# st.subheader('Cumulative VSO Unlocks per Date')
# st.bar_chart(df.rename(columns={'Date of Unlock':'index'}).set_index('index')['Cumulative VSO Amount'])

# old way of plotting unlocks
pivot_chart = pivot_table.unstack().plot(kind='bar', stacked=True)

# add bars
st.subheader('VSO Unlocks per Date')


fig = px.bar(pivot_table,
             x = pivot_table.index,
             y = [c for c in pivot_table.columns],
             template = 'plotly_dark',
             color_discrete_sequence = colors,
             # title = 'VSO Unlocks by Date',
             height=800,
             width=1500
             )

fig.update_traces(marker_line_width=1.5)
# fig.update_layout(barmode='stack')
st.plotly_chart(fig)








# VSO Pool2s Numbers
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## VSO Pool2s Liquidity and Volume")
# load parameters for the covalenthq API url
API_KEY = 'ckey_e1328ce2b7104ccaa03d0955258'
chain_id = 43114
contract_address = '0x84cf8ef74974399b4473bcf474507fe9557250ab'
page_size = 200_000
payload = {
                "key": API_KEY,
                "page-size": page_size,
                "block-signed-at-asc": True
            }


# load VSO-ELK Pool on ELk Finance from covalenthq API
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_elk_finance['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_elk_finance['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'ELK':
        balance_elk = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_elk_finance['elk_balance'].append(balance_elk)

        quote_rate_elk = item['quote_rate']
        # df_elk_finance['elk_quote_rate'].append(quote_rate_elk)
        continue


st.markdown("### VSO-ELK Elk Finance")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**ELK Amount**")
    number1 = str(f'{balance_elk:,}') + ' ELK'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_elk * quote_rate_elk)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Pangolin from covalenthq API
contract_address = '0x2b532bC0aFAe65dA57eccFB14ff46d16a12de5E6'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### VSO-WAVAX Pangolin")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**WAVAX Amount**")
    number1 = str(f'{balance_wavax:,}') + ' WAVAX'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_wavax * quote_rate_wavax)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


# load PNG-VSO Pool on Pangolin from covalenthq API
contract_address = '0x9D472e21f6589380B21C42674B3585C47b74c891'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue


    if item['contract_ticker_symbol'] == 'PNG':
        balance_png = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_png = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### PNG-VSO Pangolin")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**PNG Amount**")
    number1 = str(f'{balance_png:,}') + ' PNG'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_png * quote_rate_png)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Lydia Finance from covalenthq API
contract_address = '0x4C9b23dFFF6a15cad84008ecf5B424B715D8E82C'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("### VSO-WAVAX Lydia Finance")
first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)

with first_kpi:
    st.markdown("**VSO Amount**")
    number1 = str(f'{balance_vso:,}') + ' VSO'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**WAVAX Amount**")
    number1 = str(f'{balance_wavax:,}') + ' WAVAX'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Total Liquidity in USD**")
    total_liq = float("{:.2f}".format((balance_vso * quote_rate_vso) + (balance_wavax * quote_rate_wavax)))
    number1 = str(f'{total_liq:,}') + ' USD'
    st.markdown(f"<h1 style='text-align: left; color: red;'>{number1}</h1>", unsafe_allow_html=True)


# load VSO-WAVAX Pool on Trader Joe from covalenthq API
contract_address = '0x00979bd14bd5eb5c456c5478d3bf4b6e9212ba7d'
covalent_url = 'https://api.covalenthq.com/v1/' + str(chain_id) + "/address/" + contract_address + '/balances_v2/?quote-currency=usd'
url = requests.get(url=covalent_url, params=payload)

# load data for pool contract address
items = url.json()['data']['items']

for item in items:
    if item['contract_ticker_symbol'] == 'VSO':
        balance_vso = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['vso_balance'].append(balance_vso)

        quote_rate_vso = item['quote_rate']
        # df_pangolin['vso_quote_rate'].append(quote_rate_vso)
        continue

    if item['contract_ticker_symbol'] == 'WAVAX':
        balance_wavax = float("{:.2f}".format(float(item['balance']) / 10 ** 18))
        # df_pangolin['elk_balance'].append(balance_wavax)

        quote_rate_wavax = item['quote_rate']
        # df_pangolin['elk_quote_rate'].append(quote_rate_wavax)
        continue


print('hi')