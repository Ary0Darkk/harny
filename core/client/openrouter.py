import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
# print(api_key)

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    data=json.dumps(
        {
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages": [
                {
                    "role": "user",
                    "content": "How many r's are in the word 'strawberry'?",
                }
            ],
            "reasoning": {"enabled": True},
        }
    ),
)

response.raise_for_status()

# Extract the assistant message with reasoning_details
response = response.json()
response = response["choices"][0]["message"]["content"]
print(response)


# --- Response sample ---

# {
#     "id": "gen-1781261906-j0swjGTVgXAfREtbsYHx",
#     "object": "chat.completion",
#     "created": 1781261906,
#     "model": "nvidia/nemotron-3-super-120b-a12b-20230311:free",
#     "provider": "Nvidia",
#     "system_fingerprint": "vllm-0.22.1-tp4-ecb7cc45",
#     "service_tier": None,
#     "choices": [
#         {
#             "index": 0,
#             "logprobs": None,
#             "finish_reason": "stop",
#             "native_finish_reason": "stop",
#             "message": {
#                 "role": "assistant",
#                 "content": "The word \"strawberry\" is spelled: **S-T-R-A-W-B-E-R-R-Y**.\n\nCounting the 'r's:\n- Position 3: 'r' (in \"str\")\n- Position 8: 'r' (first 'r' in \"rr\")\n- Position 9: 'r' (second 'r' in \"rr\")\n\nThis gives a total of **3 'r's**.\n\n**Answer: 3**",
#                 "refusal": None,
#                 "reasoning": "Okay, the user is asking how many 'r's are in the word \"strawberry\". Let me think about this carefully.\n\nFirst, I need to spell out the word \"strawberry\" to count the r's. Let me write it down: S-T-R-A-W-B-E-R-R-Y.\n\nNow, I'll go through each letter one by one to count the r's.\n\nStarting with S - not an r.\nT - not an r.\nR - that's the first r.\nA - not an r.\nW - not an r.\nB - not an r.\nE - not an r.\nR - that's the second r.\nR - that's the third r.\nY - not an r.\n\nSo I have three r's: positions 3, 8, and 9 in the word.\n\nLet me double-check: s-t-r-a-w-b-e-r-r-y. Yes, after the 'e' there are two r's in a row, plus the one after the 't'. So that's three r's total.\n\nI recall that sometimes people might miscount because of the double r at the end, but no, it's clearly three: one in \"str\" and two in \"berry\".\n\nThe word is \"strawberry\" - straw has one r (s-t-r), and berry has two r's (b-e-r-r-y). So 1 + 2 = 3.\n\nI think that's correct. The user might be testing attention to detail, or perhaps they've heard a trick question about this word before. But in reality, it's straightforward.\n\nJust to be absolutely sure, let me consider if there's any alternative spelling or pronunciation issue, but no, the standard English spelling is s-t-r-a-w-b-e-r-r-y.\n\nSo the answer should be 3.\n\nThe user asked for the number of r's, and I've confirmed it's three. I should present this clearly in my response.\n\n",
#                 "reasoning_details": [
#                     {
#                         "type": "reasoning.text",
#                         "text": "Okay, the user is asking how many 'r's are in the word \"strawberry\". Let me think about this carefully.\n\nFirst, I need to spell out the word \"strawberry\" to count the r's. Let me write it down: S-T-R-A-W-B-E-R-R-Y.\n\nNow, I'll go through each letter one by one to count the r's.\n\nStarting with S - not an r.\nT - not an r.\nR - that's the first r.\nA - not an r.\nW - not an r.\nB - not an r.\nE - not an r.\nR - that's the second r.\nR - that's the third r.\nY - not an r.\n\nSo I have three r's: positions 3, 8, and 9 in the word.\n\nLet me double-check: s-t-r-a-w-b-e-r-r-y. Yes, after the 'e' there are two r's in a row, plus the one after the 't'. So that's three r's total.\n\nI recall that sometimes people might miscount because of the double r at the end, but no, it's clearly three: one in \"str\" and two in \"berry\".\n\nThe word is \"strawberry\" - straw has one r (s-t-r), and berry has two r's (b-e-r-r-y). So 1 + 2 = 3.\n\nI think that's correct. The user might be testing attention to detail, or perhaps they've heard a trick question about this word before. But in reality, it's straightforward.\n\nJust to be absolutely sure, let me consider if there's any alternative spelling or pronunciation issue, but no, the standard English spelling is s-t-r-a-w-b-e-r-r-y.\n\nSo the answer should be 3.\n\nThe user asked for the number of r's, and I've confirmed it's three. I should present this clearly in my response.\n\n",
#                         "format": "unknown",
#                         "index": 0,
#                     }
#                 ],
#             },
#         }
#     ],
#     "usage": {
#         "prompt_tokens": 30,
#         "completion_tokens": 501,
#         "total_tokens": 531,
#         "cost": 0,
#         "is_byok": False,
#         "prompt_tokens_details": {
#             "cached_tokens": 0,
#             "cache_write_tokens": 0,
#             "audio_tokens": 0,
#             "video_tokens": 0,
#         },
#         "cost_details": {
#             "upstream_inference_cost": 0,
#             "upstream_inference_prompt_cost": 0,
#             "upstream_inference_completions_cost": 0,
#         },
#         "completion_tokens_details": {
#             "reasoning_tokens": 375,
#             "image_tokens": 0,
#             "audio_tokens": 0,
#         },
#     },
# }
