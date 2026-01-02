using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class TextChatTestUI : MonoBehaviour
{
    [SerializeField] private TMP_InputField inputField;
    [SerializeField] private Button sendButton;
    [SerializeField] private TextMeshProUGUI debugText;
    [SerializeField] private ConversationManager conversationManager;

    private void Awake()
    {
        sendButton.onClick.AddListener(OnSendClicked);
    }

    private void OnSendClicked()
    {
        if (string.IsNullOrWhiteSpace(inputField.text))
            return;

        debugText.text = "You: " + inputField.text;
        conversationManager.SendUserMessage(inputField.text);
        inputField.text = "";
        inputField.ActivateInputField();
    }

    public void SetAIResponse(string response)
    {
        debugText.text += "\nAI: " + response;
    }
}
