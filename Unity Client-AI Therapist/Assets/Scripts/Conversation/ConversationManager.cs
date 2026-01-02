using UnityEngine;

public class ConversationManager : MonoBehaviour
{
    [Header("References")]
    [SerializeField] private FlaskClient flaskClient;

    [Header("State")]
    [SerializeField] private PersonaProfile activePersona;
    [SerializeField] private TextChatTestUI testUI;

    private string sessionId;

    public void SetPersona(PersonaProfile persona)
    {
        activePersona = persona;
    }

    public void SendUserMessage(string text)
    {
        if (string.IsNullOrWhiteSpace(text) || activePersona == null)
            return;

        StartCoroutine(flaskClient.SendMessage(
            text,
            activePersona.personaId,
            sessionId,
            OnAIReply,
            OnError
        ));
    }

    private void OnAIReply(string reply, string newSessionId)
{
    sessionId = newSessionId;
    Debug.Log($"AI ({activePersona.displayName}): {reply}");

    if (testUI != null)
        testUI.SetAIResponse(reply);
}


    private void OnError(string error)
    {
        Debug.LogError("Flask Error: " + error);
    }
}
