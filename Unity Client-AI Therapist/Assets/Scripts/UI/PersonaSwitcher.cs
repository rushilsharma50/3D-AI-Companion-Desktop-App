using UnityEngine;
using UnityEngine.UI;

public class PersonaSwitcher : MonoBehaviour
{
    [SerializeField] private ConversationManager conversationManager;

    [Header("Persona Assets")]
    public PersonaProfile arjun;
    public PersonaProfile mira;
    public PersonaProfile lina;
    public PersonaProfile nova;

    public void SetArjun() => conversationManager.SetPersona(arjun);
    public void SetMira()  => conversationManager.SetPersona(mira);
    public void SetLina()  => conversationManager.SetPersona(lina);
    public void SetNova()  => conversationManager.SetPersona(nova);
}
