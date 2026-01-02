using UnityEngine;

[CreateAssetMenu(menuName = "AURA/Persona Profile")]
public class PersonaProfile : ScriptableObject
{
    [Header("Identity")]
    public string personaId;     // sent to Flask
    public string displayName;   // UI only

    [Header("Voice Constraints")]
    public int maxWords = 25;
    public float maxSpeechSeconds = 6f;

    [Header("Behavior Flags")]
    public bool emotional;
    public bool allowsAffection;
}
