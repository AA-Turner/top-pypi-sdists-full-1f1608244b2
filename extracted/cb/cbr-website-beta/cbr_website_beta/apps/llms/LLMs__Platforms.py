from osbot_utils.base_classes.Type_Safe import Type_Safe


class LLMs__Platforms(Type_Safe):

    def model_options(self):
        return { 'Groq (Free)'       : { '1. Meta'      : { '1. Llama 3.2 11B Vision'      : 'llama-3.2-11b-vision-preview'                ,
                                                            '2. Llama 3.2 1B'              : 'llama-3.2-1b-preview'                        ,
                                                            '3. LLaMA 3.1 70B'             : 'llama-3.1-70b-versatile'                     ,
                                                            '4. LLaMA 3.1 8B'              : 'llama-3.1-8b-instant'                        ,
                                                            '5, LLaMA 3 70b'               : 'llama3-70b-8192'                             ,
                                                            '6. LLaMA 3 8b'                : 'llama3-8b-8192'                              ,
                                                            # 'Llama 3.2 90B'              : 'llama-3.2-90b-vision-preview'                , # "Coming Soon"
                                                            #'Llama 3.2 3B'                : 'llama-3.2-3b-preview'                        ,  # errors with: Error fetching Open Router data : 'NoneType' object is not subscriptable
                                                            # 'Llama 3.1 405B'             : 'llama-3.1-405b-reasoning'                    ,  # "Offline due to overwhelming demand! "
                                                            },
                                         '2. Mistral'   : { 'Mixtral 8x7b'                 : 'mixtral-8x7b-32768'                          },
                                         '3. Google'    : { 'Gemma 7b'                     : 'gemma-7b-it'                                 ,
                                                            'Gemma2 9b'                    : 'gemma2-9b-it'                                },
                                         '4. Groq'      : { 'LLaMA3 Groq 8b Tool'          : 'llama3-groq-8b-8192-tool-use-preview'        ,
                                                            'LLaMA3 Groq 70b Tool'         : 'llama3-groq-70b-8192-tool-use-preview'       }},

                 'SambaNova (Free)'  : {'Meta'          : { '1. Llama 3.1 8B (8k)'         : 'Meta-Llama-3.1-8B-Instruct-8k'               ,
                                                            '2. Llama 3.2 1B'              : 'Meta-Llama-3.2-1B-Instruct'                  ,
                                                            '3. Llama 3.2 3B'              : 'Meta-Llama-3.2-3B-Instruct'                  ,
                                                            '4. Llama 3.1 70B (8k)'        : 'Meta-Llama-3.1-70B-Instruct-8k'              ,
                                                            '5. Llama 3.1 405B (8k)'       : 'Meta-Llama-3.1-405B-Instruct-8k'             }},

                 'Open Router (Free)': { 'Google'       : { #'Gemini Experimental 1121'     : 'google/gemini-exp-1121:free '                 ,
                                                            #'Gemma 7b'                     : 'google/gemma-7b-it:free'                      ,
                                                            'Gemma 9b'                     : 'google/gemma-2-9b-it:free'                    ,
                                                            #'Gemini Flash 8B 1.5 Exp'      : 'google/gemini-flash-8b-1.5-exp'               ,
                                                            #'Gemini Flash 1.5 Exp'         : 'google/gemini-flash-1.5-exp'                  ,
                                                                                                                                            },
                                         'Meta'         : { 'LLaMA3 8b'                    : 'meta-llama/llama-3-8b-instruct:free'          ,
                                                            'Llama 3.1 8B Instruct'        : 'meta-llama/llama-3.1-8b-instruct:free'        ,
                                                            'Llama 3.2 3B Instruct'        : 'meta-llama/llama-3.2-3b-instruct:free'        ,
                                                            'Llama 3.2 11B Vision Instruct': 'meta-llama/llama-3.2-11b-vision-instruct:free'},
                                         'Liquid'       : { 'LFM 40B MoE'                  : 'liquid/lfm-40b:free'                          },
                                         'Microsoft'    : { 'Phi-3 Medium 128K'            : 'microsoft/phi-3-medium-128k-instruct:free'    ,
                                                            'Phi-3 Mini 128K'              : 'microsoft/phi-3-mini-128k-instruct:free'      },
                                         'Nous Research': { 'Capybara 7b'                  : 'nousresearch/nous-capybara-7b:free'           ,
                                                            'Hermes 3 405B Instruct (Ex)'  : 'nousresearch/hermes-3-llama-3.1-405b:extended',
                                                            'Hermes 3 405B Instruct'       : 'nousresearch/hermes-3-llama-3.1-405b'         },
                                         'Open Chat'    : { 'Openchat 7b'                  : 'openchat/openchat-7b:free'                    },
                                         'Gryphe'       : { 'Mythomist 7b'                 : 'gryphe/mythomist-7b:free'                     },
                                         'Wild 7B'      : { 'Toppy M 7b'                   : 'undi95/toppy-m-7b:free'                       },
                                         'Hugging Face' : { 'Zephyr 7b'                    : 'huggingfaceh4/zephyr-7b-beta:free'            },
                                         'Mistral'      : { 'Mistral 7b Instruct'          : 'mistralai/mistral-7b-instruct:free'           ,
                                                            'Pixtral 12B'                  : 'mistralai/pixtral-12b:free'                   }},
                'Open Router (Paid)' : { 'Qwen'         : { 'Qwen 2 7B Instruct'           : 'qwen/qwen-2-7b-instruct'                      ,
                                                            'Qwen 2 72B'                   : 'qwen/qwen-2-72b-instruct'                     },
                                         'Anthropic'    : { 'Claude Instant v1'            : 'anthropic/claude-instant-1:beta'              ,
                                                            'Claude 3.5 Sonnet'            : 'anthropic/claude-3.5-sonnet'                  },
                                         'Cohere'       : { 'Command R (08-2024)'          : 'cohere/command-r-08-2024'                     },
                                         'Gryphe'       : { 'MythoMax 13b'                 : 'gryphe/mythomax-l2-13b'                       },
                                         'Meta'         : { 'Llama 3.1 405B Instruct'      : 'meta-llama/llama-3.1-405b-instruct'           ,
                                                            'Llama 3.1 8B Instruct'        : 'meta-llama/llama-3.1-8b-instruct'             ,
                                                            'Llama 3.1 70B Instruct'       : 'meta-llama/llama-3.1-70b-instruct'            },
                                         'Mistral'      : { 'Ministral 8B'                 : 'mistralai/ministral-8b'                       ,
                                                            'Ministral 3B'                 : 'mistralai/ministral-3b'                       ,
                                                            'Mistral Nemo'                 : 'mistralai/mistral-nemo'                       ,
                                                            'Codestral Mamba'              : 'mistralai/codestral-mamba'                    ,
                                                            'Mistral Large'                : 'mistralai/mistral-large'                      },
                                         'Nous Research': { 'Hermes 2 7b'                  : 'nousresearch/hermes-2-theta-llama-3-8b'       },
                                         'Microsoft'    : { 'Phi-3.5 Mini 128K Instruct'   : 'microsoft/phi-3.5-mini-128k-instruct'         ,
                                                            'WizardLM-2 8x22b'             : 'microsoft/wizardlm-2-8x22b'                   },
                                         'Nvidia'       : { 'Llama 3.1 Nemotron 70B Inst'  : 'nvidia/llama-3.1-nemotron-70b-instruct'       },
                                         'Perplexity'   : { 'Llama 3.1 Sonar 8B Online'    : 'perplexity/llama-3.1-sonar-small-128k-online' ,
                                                            'Llama 3.1 Sonar 70B Online'   : 'perplexity/llama-3.1-sonar-large-128k-online' ,
                                                            'Llama 3.1 Sonar 405B Online'  : 'perplexity/llama-3.1-sonar-huge-128k-online'  },
                                         'Google'       : { 'Gemini 1.5 Flash-8B'          : 'google/gemini-flash-1.5-8b'                   ,
                                                            'Gemma 2 27B'                  : 'google/gemma-2-27b-it'                        ,
                                                            'Gemini Flash 1.5'             : 'google/gemini-flash-1.5'                      ,
                                                            'Gemini Pro 1.5 (Exp)'        : 'google/gemini-pro-1.5-exp'                     ,      # BUG: was returning: Error fetching Open Router data : 'NoneType' object is not subscriptable
                                                            'Gemma 9b'                     : 'google/gemma-2-9b-it'                         },
                                         'Sao10K'       : { 'LLaMA3 Euryale 70b'           : 'sao10k/l3-euryale-70b'                        },
                                         'Open AI'      : { 'ChatGPT-4o'                   : 'openai/chatgpt-4o-latest'                     ,
                                                            'GPT 4o-mini'                  : 'openai/gpt-4o-mini'                           ,
                                                            'GPT-4o (2024-08-06)'          : 'openai/gpt-4o-2024-08-06'                     },
#                                                            'o1-preview'                  : 'openai/o1-preview'                            ,    # quite expensive at the moment, and doesn't stream (needs separate environment) Updated Sep 12 128,000 context $15/M input tokens $60/M output tokens
#                                                            'o1-mini'                     : 'openai/o1-mini'                               },   # a bit more expensive than the other models and also doesn't support streaming: Updated Sep 12 128,000 context $3/M input tokens $12/M output tokens
                                         'Cognitive'    : { 'Dolphin Llama 3 70B'          : 'cognitivecomputations/dolphin-llama-3-70b'    }},

                 'Ollama (Local)'    : { 'Meta'         : { 'LLaMA3.2'                     : 'llama3.2:latest'                               ,
                                                            'LLaMA3.2 (vision)'            : 'llama3.2-vision:latest',
                                                            'LLaMA3 8b'                    : 'llama3'                                        ,
                                                            'Code LLaMa'                   : 'codellama'                                     },
                                         'Mistral'      : { 'Mistral'                      : 'mistral'                                       },
                                         'Microsoft'    : { 'Phi 3b (Mini)'                : 'phi3'                                          },
                                         'Google'       : { 'Gemma 2 '                     : 'gemma2:latest'                                        }},

                 'OpenAI (Paid)'     : { 'OpenAI'       : { #'o1-preview'                  : 'o1-preview'                                  ,         # not working at the moment : Your organization must qualify for at least usage tier 5 to access 'o1-preview'
                                                            #'o1-mini'                     : 'o1-mini'                                     ,
                                                            'GPT 4o-mini'                  : 'gpt-4o-mini'                                 ,
                                                            'GPT 4o'                       : 'gpt-4o'                                      ,
                                                            'GPT 4o (Structured Outputs)'  : 'gpt-4o-2024-08-06'                           ,
                                                            'GPT 4 Turbo'                  : 'gpt-4-turbo'                                 ,
                                                            'GPT 3.5 Turbo'                : 'gpt-3.5-turbo'                               }},
                 'Together AI (Paid)': { 'Meta'         : { 'LLaMA3 70b HF'                : 'meta-llama/Llama-3-70b-chat-hf'             },
                                         'Qwen'         : { 'Qwen2 72B'                    : 'Qwen/Qwen2-72B-Instruct'                    ,
                                                            'Qwen1.5 110B'                 : 'Qwen/Qwen1.5-110B-Chat'                     },
                                         'Mistral AI'   : { 'Mistral-7B'                   : 'mistralai/Mistral-7B-Instruct-v0.3'         },
                                         #'Together'     : { #'StripedHyena 7B'            : 'togethercomputer/StripedHyena-Nous-7B'       ,       # don't work
                                                            #'Evo 1 8k'                    : 'togethercomputer/evo-1-8k-base'             ,}       # don't work},
                                         'Deepseek AI'  : {'Deepseek LLM 67b'              : 'deepseek-ai/deepseek-llm-67b-chat'          },
                                         'Snowflake'    : {'Arctic Instruct'               : 'Snowflake/snowflake-arctic-instruct'        },
                                         'Databricks'   : {'DBRX Instruct'                 : 'databricks/dbrx-instruct'                   }},
                'Mistral (Free)'     : { 'Mistral'      : {'Pixtral'                       : 'pixtral-12b-2409'                           ,
                                                           'Mistral Nemo'                  : 'open-mistral-nemo'                          ,
                                                           'Codestral Mamba'               : 'open-codestral-mamba'                       }}}


