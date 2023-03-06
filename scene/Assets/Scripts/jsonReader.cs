using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class jsonReader : MonoBehaviour
{

    public TextAsset textJSON;

    [System.Serializable]
    public class User
    {
        public string user;
        public int xpos;
        public int ypos;
        public string emotion;

    }

    [System.Serializable]
    public class userList 
    {
        public User[] Users;
    }

    public userList myUsers = new userList();

    // Start is called before the first frame update
    void Start()
    {
        myUsers = JsonUtility.FromJson<userList>(textJSON.text); 
    }

    // Update is called once per frame
    void Update()
    {

        myUsers = JsonUtility.FromJson<userList>(textJSON.text);

    }
}
   